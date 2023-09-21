from Infraestructure.Parser import Parser
from Infraestructure.ChromosomeCoding import ChromosomeCoding
from Infraestructure.ChromosomeRating import ChromosomeRating

def main():
    # Busca e internaliza os dados dos professores e turmas
    parser = Parser()
    lista_cursos, lista_disponibilidade, lista_todas_disciplinas = parser.process_configs()
    print(str(len(lista_cursos)) + ' - ' + str(len(lista_disponibilidade)))

    # Recebe a lista de cursos e a população inicial
    # Faz a montagem dos cromossomos por curso
    chromesome = ChromosomeCoding(10)
    lista_cromossomos = chromesome.process_initial_chromosomes(lista_cursos)
    descontos = ChromosomeRating.av_carga_horaria(lista_cromossomos, lista_todas_disciplinas, lista_cursos)
    print(str(len(lista_cromossomos)))
    print(str(len(lista_cromossomos[0])))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
