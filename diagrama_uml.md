```mermaid
classDiagram
    %% ===== Exceções Personalizadas =====
    class Exception {
        <<built-in>>
    }
    class CodeQuestError {
        <<exception>>
    }
    class InventarioCheioError {
        <<exception>>
    }
    class AcaoInvalidaError {
        <<exception>>
    }
    Exception <|-- CodeQuestError
    CodeQuestError <|-- InventarioCheioError
    CodeQuestError <|-- AcaoInvalidaError

    %% ===== Enums =====
    class StatusPersonagem {
        <<enumeration>>
        NORMAL
        ENVENENADO
        MORTO
    }

    class TipoAcao {
        <<enumeration>>
        ATAQUE_FISICO
        HABILIDADE_CODIGO
        CURA
    }

    class EstadoPartida {
        <<enumeration>>
        NAO_INICIADA
        EM_ANDAMENTO
        VITORIA
        GAME_OVER
    }

    %% ===== Mixins e Padrões (Observer) =====
    class ObservavelMixin {
        <<mixin>>
        -List observadores
        +adicionar_observador(observador) void
        +remover_observador(observador) void
        +notificar_observadores(evento: str, dados: dict) void
    }

    %% ===== Personagens =====
    class Personagem {
        <<abstract>>
        -str nome
        -int pontos_vida
        -int pontos_vida_max
        -int ataque
        -int defesa
        -StatusPersonagem status
        +receber_dano(int dano) int
        +curar(int quantidade) int
        +esta_vivo() bool
    }

    class Player {
        -int xp
        -int nivel
        -int vidas
        -Inventario inventario
        -List~Acao~ acoes
        -List~Equipamento~ equipamentos
        +avancar_casa(Casa casa) void
        +equipar(Equipamento equipamento) void
        +usar_consumivel(Consumivel consumivel) void
        +usar_poder(Acao poder) bool
        +acoes_disponiveis() List~Acao~
        +desbloquear_acao(Acao acao) void
        +ganhar_xp(int quantidade) void
        +subir_nivel() void
    }

    class Inimigo {
        -List~Item~ itens_loot
        -Recompensa recompensa
        +dropar_loot() List~Item~
        +escolher_acao() str
    }

    class Boss {
        -ItemChave item_chave
        +dropar_loot() List~Item~
    }

    %% ===== Itens =====
    class Item {
        <<abstract>>
        -str nome
        -str descricao
    }

    class Equipavel {
        <<mixin>>
        +aplicar_bonus(Player jogador) void
        +remover_bonus(Player jogador) void
    }

    class Empilhavel {
        <<mixin>>
        -int quantidade
        +aumentar(int valor) void
        +reduzir(int valor) void
        +esta_esgotado() bool
    }

    class ItemChave {
        -str conceito_programacao
    }

    class Equipamento {
        -int bonus_ataque
        -int bonus_defesa
        -str tipo_bonus
        -bool equipado
        +equipar(Player jogador) void
        +desequipar(Player jogador) void
    }

    class Consumivel {
        -int efeito
        +usar(Player jogador) void
    }

    class Inventario {
        -int capacidade_slots
        -List~Item~ itens
        +adicionar(Item item) bool
        +remover(Item item) void
        +esta_cheio() bool
        -empilhar(Item item) bool
        -descartar(Item item) void
    }

    class Recompensa {
        -int xp
        -Item item
        -Acao acao_desbloqueada
        +aplicar(Player jogador) void
    }

    %% ===== Ações e desafios (Strategy) =====
    class Acao {
        <<abstract>>
        -str nome
        -TipoAcao tipo
        -bool desbloqueada
        -Desafio desafio
        +executar(Player jogador, Inimigo alvo) bool
        #aplicar_efeito(Player jogador, Inimigo alvo) void
    }

    class Atacar {
        #aplicar_efeito(Player jogador, Inimigo alvo) void
    }

    class Defender {
        #aplicar_efeito(Player jogador, Inimigo alvo) void
    }

    class UsarPoder {
        #aplicar_efeito(Player jogador, Inimigo alvo) void
    }

    class Desafio {
        -str enunciado
        -str codigo_inicial
        -List~str~ testes
    }

    class EditorDeCodigo {
        -str codigo_atual
        +definir_codigo_inicial(str codigo) void
        +obter_codigo() str
        +enviar_para_avaliacao() bool
    }

    %% ===== Avaliação (DIP) =====
    class IAvaliadorCodigo {
        <<interface>>
        +avaliar(str codigo, Desafio desafio) bool
    }

    class AvaliadorSubprocessoLocal {
        -int timeout_segundos
        +avaliar(str codigo, Desafio desafio) bool
        -executar_isolado(str codigo) bool
    }

    class AvaliadorMock {
        -bool resultado_simulado
        +avaliar(str codigo, Desafio desafio) bool
    }

    %% ===== Estrutura do jogo =====
    class Trilha {
        -str nome
        -List~Regiao~ regioes
        +obter_regiao(int indice) Regiao
        +proxima_regiao(Regiao atual) Regiao
    }

    class Regiao {
        -str nome
        -str conteudo_python
        -List~Casa~ casas
        -Boss boss
        -ItemChave item_chave_necessario
        +casa_inicial() Casa
        +casa_final() CasaDeBatalha
        +liberada_para(Player jogador) bool
        +esta_concluida() bool
    }

    %% ===== Casas (Template Method) =====
    class Casa {
        <<abstract>>
        -int numero
        -Desafio desafio
        -bool concluida
        +iniciar(Player jogador) void
        +reiniciar_desafio() void
        +pode_concluir() bool
        +concluir(bool aprovado) void
        #tratar_aprovacao() void
        #tratar_reprovacao() void
    }

    class CasaComum {
        +pode_concluir() bool
        #tratar_reprovacao() void
    }

    class CasaDeEvento {
        -Recompensa recompensa
        -bool recompensa_perdida
        +conceder_recompensa(Player jogador) void
        #tratar_reprovacao() void
    }

    class CasaDeBatalha {
        -Inimigo inimigo
        +pode_concluir() bool
        +iniciar_batalha(Player jogador) Batalha
        #tratar_reprovacao() void
    }

    class Batalha {
        -int turno
        -Player jogador
        -Inimigo inimigo
        +executar_turno(Acao acao) void
        +terminou() bool
        +vencedor() Personagem
    }

    %% ===== Fábrica (Factory Method) =====
    class FabricaDeEntidades {
        +criar_inimigo(Regiao regiao) Inimigo
        +criar_boss(Regiao regiao) Boss
        +criar_item(str tipo) Item
    }

    %% ===== Partida e persistência (Repository / DIP) =====
    class Partida {
        -Player jogador
        -Trilha trilha
        -Casa casa_atual
        -Batalha batalha_atual
        -EstadoPartida estado
        +iniciar() void
        +avancar() void
        +finalizar() void
    }

    class IRepositorioProgresso {
        <<interface>>
        +salvar(Partida partida) bool
        +carregar() Partida
        +atualizar(Partida partida) bool
        +excluir() bool
    }

    class RepositorioJSON {
        -str caminho_arquivo
        +salvar(Partida partida) bool
        +carregar() Partida
        +atualizar(Partida partida) bool
        +excluir() bool
    }

    class RepositorioMemoria {
        -Partida partida_guardada
        +salvar(Partida partida) bool
        +carregar() Partida
        +atualizar(Partida partida) bool
        +excluir() bool
    }

    %% ===== Relações de Herança =====
    Personagem <|-- Player
    ObservavelMixin <|-- Player : herança múltipla
    Personagem <|-- Inimigo
    Inimigo <|-- Boss
    Item <|-- ItemChave
    Item <|-- Equipamento
    Item <|-- Consumivel
    Equipavel <|-- Equipamento : herança múltipla
    Empilhavel <|-- Consumivel : herança múltipla
    Acao <|-- Atacar
    Acao <|-- Defender
    Acao <|-- UsarPoder
    Casa <|-- CasaComum
    Casa <|-- CasaDeEvento
    Casa <|-- CasaDeBatalha
    IAvaliadorCodigo <|.. AvaliadorSubprocessoLocal
    IAvaliadorCodigo <|.. AvaliadorMock
    IRepositorioProgresso <|.. RepositorioJSON
    IRepositorioProgresso <|.. RepositorioMemoria

    %% ===== Composição e Agregação =====
    Player "1" *-- "1" Inventario : compõe
    Player "0..1" o-- "0..*" Equipamento : agrega
    Player "0..1" o-- "0..*" Acao : agrega
    Inventario "1" o-- "0..*" Item : agrega
    Partida "1" *-- "1" Trilha : compõe
    Trilha "1" *-- "1..*" Regiao : compõe
    Regiao "1" *-- "1..*" Casa : compõe
    Casa "0..1" *-- "1" Desafio : compõe
    Desafio "1" *-- "1" EditorDeCodigo : compõe
    EditorDeCodigo "1" *-- "1" IAvaliadorCodigo : compõe
    Batalha "0..1" o-- "1" Player : agrega
    Batalha "0..1" o-- "1" Inimigo : agrega

    %% ===== Associações e dependências =====
    Recompensa "0..1" --> "0..1" Item : concede
    Recompensa "0..1" --> "0..1" Acao : desbloqueia
    Recompensa ..> Player : recebe
    Inimigo "0..1" --> "0..1" Recompensa : entrega ao ser derrotado
    Inimigo "0..1" --> "1..*" Item : dropa ao ser derrotado
    Boss "1" --> "1..*" ItemChave : dropa ao ser derrotado
    CasaDeEvento "0..1" --> "1" Recompensa : concede
    CasaDeEvento "0..1" --> "0..1" Inimigo : pode derrotar por evento especial
    CasaDeBatalha "1" --> "1" Inimigo : rival da casa
    CasaDeBatalha "1" --> "0..*" Batalha : inicia
    Acao "0..1" --> "1" Desafio : exige resolver
    Regiao "1" --> "1" Boss : possui
    Regiao "0..1" --> "0..1" ItemChave : exige para liberar
    Partida "1" --> "1" Player : controla
    Partida "0..1" --> "1" Casa : casa atual
    Partida "1" --> "0..1" Batalha : batalha em curso
    IAvaliadorCodigo ..> Desafio : testa com asserts
    Partida ..> IAvaliadorCodigo : depende de
    Batalha ..> IAvaliadorCodigo : depende de
    Batalha ..> Acao : executa
    Partida ..> IRepositorioProgresso : depende de
    IRepositorioProgresso ..> Partida : persiste o progresso
    Partida ..> FabricaDeEntidades : usa
    FabricaDeEntidades ..> Regiao : lê os dados
    FabricaDeEntidades ..> Inimigo : cria
    FabricaDeEntidades ..> Boss : cria
    FabricaDeEntidades ..> Item : cria
```
