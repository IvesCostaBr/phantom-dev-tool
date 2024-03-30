from src.integrations import gpt_manager


def exec(data):
    type_analize = data.get("payload").get("type")
    message = ""
    if type_analize == "fix":
        message = f"""Está ocorrendo um erro no meu codigo,
            para interpretar melhor remova os numeros na frente de cada linhas,
            {data.get('file_content').get('data')}, problema que está acontecendo é {data.get('payload').get('problem')}, retorna o meu codigo inteiro com a correção."""
    elif type_analize == "refact":
        message = f"""Por Favor analisa o seguinte codigo que vou mandar,
            para interpretar melhor remova os numeros na frente de cada linhas,
            {data.get('file_content').get('data')}, eu quero refatorar o meu codigo para ser mais eficiente e facil de entender, retorna o codigo todo, com as melhorias."""
    else:
        raise Exception(f"tipo de analise não reconhecida -> {type_analize}")
    response = gpt_manager.send_message(message)
    try:
        code = response
        return code.strip().split('\n')
    except:
        raise Exception("o retorno do chat não foi formatado corretamente.")
