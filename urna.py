
def solicitar_voto(tipo, candidatos):
    while True:
        voto = input(
            f'Digite o número do candidato a {tipo} '
            '(ou "1" para votar em Branco): '
        )

        if voto.isdigit():
            if voto in candidatos:
                return voto

            print(f'Voto nulo registrado para {tipo}.')
            return 'Nulo'

        print('Entrada inválida! Digite apenas números.')


def confirmar_voto(voto, tipo, candidatos):
    if voto == 'Nulo' or voto == '1':
        return True

    while True:
        print(f'Você votou em: {candidatos[voto]} para {tipo}.')
        confirmacao = input('Confirma voto? [S/N]: ').upper()

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

    print('===== INÍCIO DA VOTAÇÃO =====')

    while True:
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

        while True:
            encerramento = input(
                'Deseja encerrar a votação? [S/N]: '
            ).upper()

            if encerramento == 'S':
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

                print('\n===== VOTAÇÃO ENCERRADA =====')
                return

            if encerramento == 'N':
                break

            print('Resposta inválida! Digite S ou N.')


if __name__ == '__main__':
    main()