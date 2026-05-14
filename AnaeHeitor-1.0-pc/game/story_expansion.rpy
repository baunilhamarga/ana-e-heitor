# New route content informed by the exported WhatsApp history.
# Dialog remains in Brazilian Portuguese; code names stay in English for future maintenance.

label post_australia_route:
    call whatsapp_mosaic_intro
    call australia_distance_arc
    call france_departure_arc
    call birthday_finale
    return

label whatsapp_mosaic_intro:
    call change_pov("heitor", "O histórico virou dataset")

    scene bg desktop_code
    with fade

    show heitor focused at pov_left
    show ana college thinking at other_right

    h "Eu abri nosso histórico do WhatsApp."

    show ana college surprised
    a "Você fez o quê?"

    show heitor college amused
    h "Nada invasivo. Só o suficiente para confirmar uma hipótese."

    show ana college annoyed
    a "Se a hipótese for que eu mando muita mensagem, isso já era consenso científico."

    h "Foram 39.475 mensagens no arquivo exportado."

    show ana college embarrassed
    a "..."

    a "Tá, talvez eu tenha uma leve tendência comunicativa."

    h "E mais de cinco mil mídias entre fotos, vídeos, áudios, GIFs e figurinhas."

    show ana college happy
    a "As figurinhas são parte fundamental da nossa infraestrutura emocional."

    heitor_thought "Eu queria discordar, mas alguns sistemas críticos realmente rodam em figurinha."

    h "O plano não é transformar tudo em ata de reunião."

    h "É escolher as memórias que explicam a gente: as conversas gigantes, os dias de saudade, os surtos acadêmicos e os aeroportos."

    call whatsapp_academic_excerpt

    call whatsapp_romancezinho_excerpt

    scene bg desktop_code
    with dissolve

    show heitor focused at pov_left
    show ana college soft at other_right

    show ana college soft
    a "Então você vai usar mensagem real?"

    h "Sim, mas só trechos escolhidos. Um print emocional, não um dump de produção."

    show ana college super_happy
    a "Finalmente uma arquitetura com LGPD romântica."

    $ add_love(5, "histórico do WhatsApp mapeado")
    return

label australia_distance_arc:
    call change_pov("heitor", "Austrália: fuso, saudade e Wi-Fi")

    scene bg airport
    with fade

    show heitor home serious at pov_left

    heitor_thought "Eu tinha prometido voltar. O problema das promessas é que elas continuam fazendo barulho dentro da mala."

    scene bg desktop_code
    with dissolve

    show heitor focused at pov_left

    h "A Austrália era longe de um jeito quase ofensivo."

    h "Quando eu acordava, ela às vezes estava dormindo. Quando ela tinha tempo, eu estava tentando não parecer um zumbi no estágio."

    heitor_thought "Engenharia de computação tinha me preparado para muita coisa. Menos para calcular saudade com fuso horário."

    call whatsapp_australia_excerpt

    scene bg desktop_code
    with dissolve

    show heitor focused at pov_left

    menu:
        "Mandar bom dia":
            h "Bom dia, amor."
            heitor_thought "Tecnicamente talvez fosse boa noite. Mas a intenção compila."
            $ add_love(3, "bom dia transcontinental")

        "Mandar boa noite":
            h "Boa noite, minha lindinha."
            heitor_thought "Se ela acordar agora, isso vira bom dia retroativo."
            $ add_love(3, "boa noite transcontinental")

        "Mandar bom dia e boa noite":
            h "Bom dia e boa noite, para garantir cobertura total de fuso."
            $ add_love(5, "redundância afetiva")

    call change_pov("ana", "Brasil: saudade em horário local")

    scene bg bedroom_night
    with fade

    show ana home neutral at pov_left

    a "Eu fingia que estava tudo sob controle."

    show ana home sad
    a "Não estava."

    a "Eu olhava o relógio do celular como se ele fosse mudar de ideia e aproximar a Austrália."

    show ana home embarrassed
    a "Spoiler: o relógio é muito pouco colaborativo."

    show heitor home soft_smile at other_right

    h "Você comeu hoje?"

    show ana home serious
    a "Você atravessou o planeta e ainda quer fiscalizar minha alimentação?"

    h "Sim."

    show ana home soft
    a "Obrigada."

    a "A distância doeu, mas também deixou uma coisa ridiculamente clara."

    a "A gente não dependia de estar no mesmo lugar para continuar escolhendo a mesma pessoa."

    $ add_love(8, "três meses de distância")
    call free_time_phase("distancia_australia")
    return

label france_departure_arc:
    call change_pov("ana", "França: o segundo grande aeroporto")

    scene bg ap_heitor_day
    with fade

    show ana home neutral at pov_left
    show heitor home soft_smile at other_right

    a "Depois da Austrália eu achei que aeroportos já tinham gastado toda a capacidade dramática."

    show ana home serious
    a "A França discordou."

    h "É o duplo diploma."

    a "Eu sei."

    h "É uma oportunidade enorme."

    a "Eu sei também."

    call whatsapp_travel_paperwork_excerpt

    scene bg ap_heitor_day
    with dissolve

    show ana home neutral at pov_left
    show heitor home soft_smile at other_right

    show ana home serious
    a "O problema é que saber não diminui a mala."

    call change_pov("heitor", "Checklist do duplo diploma")

    scene bg desktop_code
    with dissolve

    show heitor thoughtful at pov_left

    heitor_thought "Documentos. Passaporte. Adaptador. Casaco. Coragem."

    heitor_thought "Coragem não coube em nenhuma pasta, então eu fingi que estava no drive."

    show ana home soft at other_right

    a "Você está fazendo cara de quem vai explicar um sistema distribuído para não falar de sentimento."

    h "O sistema é distribuído. Metade fica aqui."

    show ana home embarrassed
    a "Isso foi bonito. Irritantemente bonito."

    call change_pov("ana", "Última noite antes da França")

    scene bg bedroom_night
    with fade

    show ana home sad at pov_left

    a "Eu queria ser adulta, elegante e perfeitamente compreensiva."

    ana_thought "Consegui aproximadamente uma dessas coisas por três minutos."

    show heitor gentle at other_right

    h "A gente já passou por distância."

    a "Essa frase devia vir com nota de rodapé."

    h "Nota de rodapé?"

    a "Sim. 'Passar por distância não torna a próxima grátis'."

    show heitor soft_laugh
    h "Justo."

    call change_pov("heitor", "Última chamada")

    scene bg airport
    with fade

    show heitor home serious at pov_left
    show ana home sad at other_right

    heitor_thought "Eu queria dizer a frase perfeita. Uma frase que coubesse tudo: orgulho, medo, plano, amor."

    heitor_thought "Obviamente eu pensei em branco."

    h "Eu volto."

    call change_pov("ana", "Última resposta")

    scene bg airport
    with dissolve

    show ana home sad at pov_left
    show heitor home serious at other_right

    a "Eu vou te cobrar."

    h "Eu sei."

    a "E vou mandar mensagem demais."

    h "Eu conto com isso."

    show ana home soft
    a "Então vai."

    a "Mas vai sabendo que eu continuo aqui."

    h "Eu também continuo."

    show ana home emotional
    a "Mesmo longe?"

    show heitor home soft_smile
    h "Principalmente longe."

    $ add_love(10, "França e duplo diploma")
    return

label birthday_finale:
    call change_pov("heitor", "Presente de aniversário")

    scene bg ap_heitor_night
    with fade

    show heitor home soft_smile at pov_left
    show ana home happy at other_right

    h "Eu tentei pensar em um presente que chegasse perto do que você fez por mim."

    show ana home embarrassed
    a "Sem pressão."

    h "Muita pressão."

    h "Você me deu a nossa história em forma de jogo."

    h "Então eu tentei continuar o projeto com o cuidado que ele merece: mais leve, mais bobo, com mais escolhas, mas sem fingir que as partes difíceis não existiram."

    show ana home soft
    a "E com dinheiro da minha mãe?"

    h "Feature essencial. Alta fidelidade histórica."

    show ana home happy
    a "Aprovado."

    h "Feliz aniversário, Ana."

    h "Essa versão ainda deixa espaço para a gente escrever o resto. Talvez um dia com os dois POVs completos."

    h "Mas por enquanto, essa parte é minha:"

    h "Eu amo você. No bandejão, no aeroporto, no fuso horário errado e em qualquer branch que a vida abrir."

    show ana home emotional
    a "Eu também amo você."

    scene black
    with fade

    system_line "Fim desta versão. A história continua."

    hide screen relationship_hud
    return
