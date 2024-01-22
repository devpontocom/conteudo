import json

import requests

VIA_CEP_URL = "http://www.viacep.com.br/ws/{}/json"


def consulta_cep(cep):
    response = requests.get(VIA_CEP_URL.format(cep))

    if response.ok:
        address = json.loads(response.text)

        if address.get("erro"):
            raise ValueError("CEP inválido")

        return {
            "district": address.get("bairro") or "",
            "cep": address.get("cep") or "",
            "city": address.get("localidade") or "",
            "street": address.get("logradouro") or "",
            "uf": address.get("uf") or "",
            "complement": address.get("complemento") or "",
        }

    if response.status_code == 400:
        raise ValueError("Erro na chamada de API")


if __name__ == "__main__":
    print(consulta_cep(65066265))
