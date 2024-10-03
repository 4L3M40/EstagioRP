def identify_lights():
    # Inicialmente todos os interruptores estão desligados
    lights = {'A': 'desligado', 'B': 'desligado', 'C': 'desligado'}

    # Ligar o primeiro interruptor (A)
    lights['A'] = 'ligado'
    print("Liguei o interruptor A e esperei alguns minutos...")

    # Desligar o primeiro e ligar o segundo (B)
    lights['A'] = 'desligado'
    lights['B'] = 'ligado'
    print("Desliguei o interruptor A e liguei o B.")

    # Simular a ida até a sala
    print("\nFui até a sala das lâmpadas.")

    # Determinar o estado das lâmpadas
    # Aqui, vamos supor que as lâmpadas A e C estão desligadas
    # e que B está ligada e quente.

    # A lâmpada B está acesa
    acesa = 'B'
    quente = 'A'
    fria = 'C'

    print(f"A lâmpada {acesa} está acesa.")
    print(f"A lâmpada {quente} estava quente, então é controlada pelo interruptor A.")
    print(f"A lâmpada {fria} está fria, controlada pelo interruptor C.")


identify_lights()
