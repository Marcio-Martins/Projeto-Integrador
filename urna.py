def solicitar_voto(tipo, candidatos):
    while True:
        voto = input(
            f'Digite o número do candidato a {tipo} '
            '(ou "1" para votar em Branco): '
        ).strip()

        if not voto.isdigit():
            print('Entrada inválida! Digite apenas números.')
            continue

        if voto in candidatos:
            return voto

        print(f'Voto nulo registrado para {tipo}.')
        return 'Nulo'


def confirmar_voto(voto, tipo, candidatos):
    if voto == 'Nulo' or voto == '1':
        return True

    while True:
        print(f'Você votou em: {candidatos[voto]} para {tipo}.')
        confirmacao = input('Confirma voto? [S/N]: ').strip().upper()

        if confirmacao == 'S':
            return True

        if confirmacao == 'N':
            return False

        print('Resposta inválida! Digite S ou N.')


def registrar_voto(voto, votos, contagem_branco, contagem_nulo):
    if voto == '1':
        contagem_branco += 1

    elif voto == 'Nulo':
        contagem_nulo += 1

    else:
        votos[voto] = votos.get(voto, 0) + 1

    return contagem_branco, contagem_nulo


def exibir_resultado(votos, candidatos, tipo, brancos, nulos):
    print(f'\n===== RESULTADO PARA {tipo.upper()} =====')

    for numero, nome in candidatos.items():
        if numero != '1':
            quantidade = votos.get(numero, 0)
            print(f'{numero} - {nome}: {quantidade} voto(s)')

    print(f'Votos brancos: {brancos}')
    print(f'Votos nulos: {nulos}')


def votar_cargo(tipo, candidatos, votos, brancos, nulos):
    while True:
        voto = solicitar_voto(tipo, candidatos)

        if confirmar_voto(voto, tipo, candidatos):
            brancos, nulos = registrar_voto(
                voto,
                votos,
                brancos,
                nulos
            )

            return brancos, nulos

        print('Voto não confirmado. Digite novamente.\n')


def votar_eleitor(
    candidatos_prefeito,
    candidatos_vereador,
    votos_prefeito,
    votos_vereador,
    brancos_prefeito,
    nulos_prefeito,
    brancos_vereador,
    nulos_vereador
):
    print('\n===== NOVO ELEITOR =====')

    (
        brancos_prefeito,
        nulos_prefeito
    ) = votar_cargo(
        'Prefeito',
        candidatos_prefeito,
        votos_prefeito,
        brancos_prefeito,
        nulos_prefeito
    )

    (
        brancos_vereador,
        nulos_vereador
    ) = votar_cargo(
        'Vereador',
        candidatos_vereador,
        votos_vereador,
        brancos_vereador,
        nulos_vereador
    )

    print('\nVotos registrados com sucesso!')

    return (
        brancos_prefeito,
        nulos_prefeito,
        brancos_vereador,
        nulos_vereador
    )


def iniciar_votacao():
    while True:
        print('\n===== CONTROLE DO MESÁRIO =====')
        print('1 - Iniciar votação')
        print('2 - Encerrar sistema')

        opcao = input('Escolha uma opção: ').strip()

        if opcao == '1':
            return True

        if opcao == '2':
            return False

        print('Opção inválida! Digite 1 ou 2.')


def controle_mesario():
    while True:
        print('\n===== CONTROLE DO MESÁRIO =====')
        print('1 - Liberar próximo eleitor')
        print('2 - Encerrar votação')

        opcao = input('Escolha uma opção: ').strip()

        if opcao == '1':
            return True

        if opcao == '2':
            return False

        print('Opção inválida! Digite 1 ou 2.')


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

    print('\n======================================')
    print('       URNA ELETRÔNICA - SIMULAÇÃO')
    print('======================================')

    votacao_iniciada = iniciar_votacao()

    if not votacao_iniciada:
        print('\nSistema encerrado pelo mesário.')
        return

    print('\n======================================')
    print('          VOTAÇÃO INICIADA')
    print('======================================')

    while True:

        (
            brancos_prefeito,
            nulos_prefeito,
            brancos_vereador,
            nulos_vereador
        ) = votar_eleitor(
            candidatos_prefeito,
            candidatos_vereador,
            votos_prefeito,
            votos_vereador,
            brancos_prefeito,
            nulos_prefeito,
            brancos_vereador,
            nulos_vereador
        )

        continuar = controle_mesario()

        if not continuar:
            break

    print('\n======================================')
    print('          VOTAÇÃO ENCERRADA')
    print('======================================')

    exibir_resultado(
        votos_prefeito,
        candidatos_prefeito,
        'Prefeito',
        brancos_prefeito,
        nulos_prefeito
    )

    exibir_resultado(
        votos_vereador,
        candidatos_vereador,
        'Vereador',
        brancos_vereador,
        nulos_vereador
    )


if __name__ == '__main__':
    main()