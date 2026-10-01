"""Renova o token de longa duracao do Instagram e grava o novo no secret do repo.

O token do Instagram vale 60 dias. Este script troca por um novo e atualiza o
secret IG_ACCESS_TOKEN via API do GitHub, que exige um PAT com permissao de
escrita em secrets (o GITHUB_TOKEN padrao nao consegue fazer isso).

O token nunca e impresso.
"""

import os
import sys
from base64 import b64encode

import requests
from nacl import encoding, public

API_BASE = "https://graph.instagram.com"
GITHUB_API = "https://api.github.com"
SECRET_NAME = "IG_ACCESS_TOKEN"


def refresh(token):
    r = requests.get(
        f"{API_BASE}/refresh_access_token",
        params={"grant_type": "ig_refresh_token", "access_token": token},
        timeout=60,
    )
    body = r.json()
    if "access_token" not in body:
        raise RuntimeError(f"falha ao renovar: {body}")
    return body["access_token"], body.get("expires_in", 0)


def encrypt_secret(public_key_b64, value):
    """Sealed box no formato que a API de secrets do GitHub espera."""
    key = public.PublicKey(public_key_b64.encode(), encoding.Base64Encoder())
    return b64encode(public.SealedBox(key).encrypt(value.encode())).decode()


def update_secret(repo, pat, value):
    headers = {
        "Authorization": f"Bearer {pat}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    r = requests.get(f"{GITHUB_API}/repos/{repo}/actions/secrets/public-key", headers=headers, timeout=30)
    r.raise_for_status()
    key = r.json()

    r = requests.put(
        f"{GITHUB_API}/repos/{repo}/actions/secrets/{SECRET_NAME}",
        headers=headers,
        json={"encrypted_value": encrypt_secret(key["key"], value), "key_id": key["key_id"]},
        timeout=30,
    )
    r.raise_for_status()


def main():
    token = os.environ.get("IG_ACCESS_TOKEN")
    pat = os.environ.get("GH_PAT")
    repo = os.environ.get("GITHUB_REPOSITORY")

    if not token or not pat or not repo:
        sys.exit("IG_ACCESS_TOKEN, GH_PAT e GITHUB_REPOSITORY sao obrigatorios")

    new_token, expires_in = refresh(token)
    update_secret(repo, pat, new_token)
    print(f"token renovado, valido por mais {expires_in // 86400} dias")


if __name__ == "__main__":
    main()
