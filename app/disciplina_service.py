from app.storage import JsonStorage


class DisciplinaService:
    def __init__(self, storage=None):
        self.storage = storage if storage else JsonStorage()

    def criar_disciplina(self, disciplina):
        self._validar_disciplina(disciplina)

        disciplinas = self.storage.read_all()

        novo_id = 1
        if disciplinas:
            novo_id = max(item["id"] for item in disciplinas) + 1

        disciplina_com_id = {
            "id": novo_id,
            "titulo": disciplina["titulo"],
            "data_inicio": disciplina["data_inicio"],
            "data_termino": disciplina["data_termino"],
            "numero_vagas": disciplina["numero_vagas"],
            "disciplina_verao": disciplina["disciplina_verao"]
        }

        disciplinas.append(disciplina_com_id)
        self.storage.write_all(disciplinas)
        return disciplina_com_id

    def listar_disciplinas(self):
        return self.storage.read_all()

    def buscar_disciplina_por_id(self, disciplina_id):
        disciplinas = self.storage.read_all()
        for disciplina in disciplinas:
            if disciplina["id"] == disciplina_id:
                return disciplina
        return None

    def atualizar_disciplina(self, disciplina_id, novos_dados):
        disciplinas = self.storage.read_all()

        for i, disciplina in enumerate(disciplinas):
            if disciplina["id"] == disciplina_id:
                disciplina_atualizada = {
                    "id": disciplina_id,
                    "titulo": novos_dados.get("titulo", disciplina["titulo"]),
                    "data_inicio": novos_dados.get("data_inicio", disciplina["data_inicio"]),
                    "data_termino": novos_dados.get("data_termino", disciplina["data_termino"]),
                    "numero_vagas": novos_dados.get("numero_vagas", disciplina["numero_vagas"]),
                    "disciplina_verao": novos_dados.get("disciplina_verao", disciplina["disciplina_verao"])
                }

                self._validar_disciplina(disciplina_atualizada)
                disciplinas[i] = disciplina_atualizada
                self.storage.write_all(disciplinas)
                return disciplina_atualizada

        return None

    def remover_disciplina(self, disciplina_id):
        disciplinas = self.storage.read_all()
        disciplinas_filtradas = [d for d in disciplinas if d["id"] != disciplina_id]

        if len(disciplinas_filtradas) == len(disciplinas):
            return False

        self.storage.write_all(disciplinas_filtradas)
        return True

    def _validar_disciplina(self, disciplina):
        campos_obrigatorios = [
            "titulo",
            "data_inicio",
            "data_termino",
            "numero_vagas",
            "disciplina_verao"
        ]

        for campo in campos_obrigatorios:
            if campo not in disciplina:
                raise ValueError(f"Campo obrigatório ausente: {campo}")

        if not disciplina["titulo"] or not isinstance(disciplina["titulo"], str):
            raise ValueError("Título inválido")

        if not isinstance(disciplina["numero_vagas"], int) or disciplina["numero_vagas"] <= 0:
            raise ValueError("Número de vagas deve ser inteiro maior que zero")

        if not isinstance(disciplina["disciplina_verao"], bool):
            raise ValueError("disciplina_verao deve ser booleano")