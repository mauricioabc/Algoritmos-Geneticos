from typing import Any


class Disciplina:
    next_id = 1

    def __init__(self, nome, fase, carga_horaria, professor):
        self.id = Disciplina.next_id
        Disciplina.next_id += 1
        self.nome = nome
        self.fase = fase
        self.carga_horaria = carga_horaria
        self.professor = professor

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

    def __str__(self) -> str:
        return super().__str__()
