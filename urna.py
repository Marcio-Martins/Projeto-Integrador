def solicitar_voto(tipo, candidatos):
    while True:
        voto = input(f'Digite o número do Candidato(a) a {tipo} (ou "1" para votar em Branco): ')
        if voto.isdigit():
            if voto in candidatos:
                return voto
            else:
                print(f'Voto nulo registrado para {tipo}.')
                return 'Nulo'
        else:
            print('Entrada inválida! Por favor, digite um número.')

def confirmar_voto(voto, tipo, candidatos):
    if voto == 'Nulo' or voto == '1':
        return True  # Nulo e Branco são automaticamente confirmados
    while True:
        print(f'Você votou em: {candidatos[voto]} para {tipo}.')
        confirmacao = input('Confirma voto? [S/N] ')
        if confirmacao.upper() == 'S':
            return True
        elif confirmacao.upper() == 'N':
            return False
        else:
            print('Resposta inválida! Digite "S" para Sim ou "N" para Não.')

def registrar_voto(voto, votos, contagem_branco, contagem_nulo):
    if voto == '1':
        contagem_branco += 1
    elif voto == 'Nulo':
        contagem_nulo += 1
    else:
        if voto in votos:
            votos[voto] += 1
        else:
            votos[voto] = 1
    return contagem_branco, contagem_nulo

def exibir_resultado(votos, candidatos, tipo, brancos, nulos):
    print(f'\nVotos para {tipo}:')
    for numero, qtd_votos in votos.items():
        print(f'{candidatos[numero]} teve {qtd_votos} votos')
    print(f'Votos brancos: {brancos}')
    print(f'Votos nulos: {nulos}')

def main():
    candidatos_prefeito = {
        '15': 'Carlos Pedro-PD',
        '21': 'Anderson Silva-PV',
        '35': 'Marta Rocha-PL',
        '1': 'Voto Branco'
    }

    candidatos_vereador = {
        '15112': 'Adriana Bela-PD',
        '15121': 'Carlos Alberto-PD',
        '15221': 'Sandro Pereira-PD',
        '15224': 'Dênis Marques-PD',
        '21123': 'Sérgio Cabral-PV',
        '21212': 'Cícero Lucena-PV',
        '21332': 'Douglas Alencar-PV',
        '35431': 'Victor Dias-PL',
        '35321': 'Vicente Oliveira-PL',
        '35551': 'Alcilina Bento-PL',
        '1': 'Voto Branco'
    }

    votos_prefeito = {}
    votos_vereador = {}
    brancos_prefeito = 0
    nulos_prefeito = 0
    brancos_vereador = 0
    nulos_vereador = 0

    print('Iniciar Votação')

    while True:
        # Votação para prefeito
        voto_prefeito = solicitar_voto('Prefeito', candidatos_prefeito)
        if confirmar_voto(voto_prefeito, 'Prefeito', candidatos_prefeito):
            brancos_prefeito, nulos_prefeito = registrar_voto(voto_prefeito, votos_prefeito, brancos_prefeito, nulos_prefeito)

        # Votação para vereador
        voto_vereador = solicitar_voto('Vereador', candidatos_vereador)
        if confirmar_voto(voto_vereador, 'Vereador', candidatos_vereador):
            brancos_vereador, nulos_vereador = registrar_voto(voto_vereador, votos_vereador, brancos_vereador, nulos_vereador)

        # Encerrar votação
        votacao = input('Deseja encerrar a votação? [S/N]: ')
        if votacao.upper() == 'S':
            break

    # Exibindo o resultado
    exibir_resultado(votos_prefeito, candidatos_prefeito, 'Prefeito', brancos_prefeito, nulos_prefeito)
    exibir_resultado(votos_vereador, candidatos_vereador, 'Vereador', brancos_vereador, nulos_vereador)

if __name__ == '__main__':
    main()
