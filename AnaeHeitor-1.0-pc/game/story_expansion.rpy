# New route content informed by the exported WhatsApp history.
# Dialog remains in Brazilian Portuguese; code names stay in English for future maintenance.

label post_australia_route:
    $ career_phase = "virtualisurg_frontend"
    $ set_love_cap_stage("post_australia")
    call whatsapp_mosaic_intro
    call australia_distance_arc
    call france_departure_arc
    call birthday_finale
    return

label whatsapp_mosaic_intro:
    $ special_day_label = "📅 Presente"
    $ current_country_label = "🇫🇷 França"
    call change_pov("heitor", "Continuando a história")

    scene bg desktop_code
    with fade

    show heitor focused at pov_left
    show ana college thinking at other_right

    h "Eu abri nosso histórico do WhatsApp."

    show ana college surprised
    a "Você fez o quê?"

    show ana college annoyed
    a "Se era pra confirmar que eu mando pouca mensagem, isso já era consenso."

    show heitor college amused
    h "Nada invasivo. Só o suficiente para continuar o melhor presente que eu já recebi."

    h "Foram 39.475 mensagens no arquivo exportado."

    show ana college embarrassed
    a "..."

    a "Tá, até que é bastante."

    h "E mais de cinco mil mídias entre fotos, vídeos, áudios, GIFs e figurinhas."

    h "E sabe quantas dessas figurinhas são repetidas de um cachorro com sorrisão mostrando os dentes?"

    show ana college annoyed
    a "Ah, para! Não sei, são quantas?"

    h "Também não sei, mas são muitas."

    show ana college happy

    h "Não foi pra transformar tudo em ata."

    h "É escolher as memórias que explicam a gente: as conversas gigantes, os dias de saudade, os surtos e os aeroportos."

    call whatsapp_academic_excerpt

    call whatsapp_romancezinho_excerpt

    scene bg desktop_code
    with dissolve

    show heitor focused at pov_left
    show ana college soft at other_right

    show ana college soft
    a "Então você vai usar mensagem real?"

    h "Sim, mas só alguns trechos. Não tem mais graça assim?"

    show ana college super_happy
    a "Uai."

    $ add_love(5, "histórico do WhatsApp mapeado")
    $ special_day_label = ""
    return

label australia_distance_arc:
    $ set_love_cap_stage("post_australia")
    $ current_country_label = "🇦🇺 Austrália"
    call change_pov("heitor", "Austrália: fuso e saudade")

    scene bg airport
    with fade

    show heitor home serious at pov_left

    heitor_thought "Eu ia voltar. Mas o problema era que eu ia sair de novo logo depois."

    scene bg desktop_code
    with dissolve

    show heitor focused at pov_left

    heitor_thought "A Austrália era longe de um jeito quase ofensivo."

    heitor_thought "Quando eu acordava, ela às vezes estava dormindo. Quando ela tinha tempo, eu estava tentando não parecer um zumbi no estágio."

    heitor_thought "A vida tinha me preparado para muita coisa. Menos para saudade."

    call whatsapp_australia_excerpt

    scene bg desktop_code
    with dissolve

    show heitor focused at pov_left

    menu:
        "Mandar bom dia":
            h "Bom dia, amor."
            heitor_thought "Tecnicamente talvez fosse boa noite. Mas vale a intenção."
            $ add_love(3, "bom dia transcontinental")

        "Mandar boa noite":
            h "Boa noite, minha lindinha."
            heitor_thought "Se ela acordar agora, isso vira bom dia retroativo."
            $ add_love(3, "boa noite transcontinental")

        "Mandar bom dia e boa noite":
            h "Bom dia e boa noite, para garantir."
            $ add_love(5, "redundância afetiva")

    call change_pov("ana", "Brasil: saudade em horário local")
    $ current_country_label = "🇧🇷 Brasil"

    scene bg bedroom_night
    with fade

    show ana home neutral at pov_left

    ana_thought "Eu fingia que estava tudo sob controle."

    show ana home sad
    ana_thought "Não estava."

    ana_thought "Eu olhava o relógio do celular como se ele fosse mudar de ideia e aproximar a Austrália."

    show ana home embarrassed
    ana_thought "Spoiler: não rolou."

    show heitor home soft_smile at other_right

    h "Você comeu hoje?"

    show ana home serious
    a "Você atravessou o planeta e ainda quer fiscalizar minha alimentação?"

    h "Sim."

    show ana home soft
    a "Obrigada."

    ana_thought "A distância doeu, mas também deixou uma coisa ridiculamente clara."

    ana_thought "A gente não dependia de estar no mesmo lugar para continuar escolhendo a mesma pessoa."

    $ add_love(8, "três meses de distância")
    if endgame_replay_mode:
        return
    call free_time_phase("distancia_australia")
    return

label france_departure_arc:
    $ set_love_cap_stage("france_departure")
    $ current_country_label = "🇧🇷 Brasil"
    call change_pov("ana", "França: o segundo grande aeroporto")

    scene bg ap_heitor_day
    with fade

    show ana home neutral at pov_left
    show heitor home soft_smile at other_right

    ana_thought "Depois da Austrália eu achei que aeroportos já tinham gastado toda a capacidade dramática."

    show ana home serious
    ana_thought "Mas a França chamou."

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
    ana_thought "O problema é saber que é tão pouco tempo comigo e ele já vai."

    call change_pov("heitor", "Checklist do duplo diploma")

    scene bg desktop_code
    with dissolve

    show heitor thoughtful at pov_left

    heitor_thought "Documentos. Passaporte. Adaptador. Casaco. Coragem."

    heitor_thought "Saudade."

    heitor_thought "Essa não tem como esquecer, vem de qualquer forma."

    show ana home soft at other_right

    a "Que cara é essa? No que você tá pensando?"

    h "Nada, olha só. Cabeça oca."

    show ana home embarrassed
    a "Ha-ha Para."

    call change_pov("ana", "Última noite antes da França")

    scene bg bedroom_night
    with fade

    show ana home sad at pov_left

    ana_thought "Eu queria ser adulta e perfeitamente compreensiva."

    ana_thought "Quase consegui por três minutos."

    show heitor gentle at other_right

    h "A gente já passou por distância."

    a "Passar por distância não torna a próxima grátis."

    show heitor thoughtful

    h "Eu sinto muito."

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

    a "Eu vou melhorar, vou mandar mensagem."

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
    $ career_phase = "virtualisurg_xr"
    return

label birthday_finale:
    $ set_love_cap_stage("birthday_finale")
    $ special_day_label = "📅 Presente"
    $ current_country_label = "🇫🇷 França"
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
    a "E cheio de joguinhos?"

    h "Essencial. Você viu que eu coloquei Jorge e Mateus?"

    if any(key.startswith("propaganda_") for key in rhythm_best_results.keys()):
        # If the player has already seen the Jorge e Mateus DDR minigame, this line will be shown instead.
        a "Simmmm, eu quase gritei quando eu vi."

        h "Eu achei que você ia gostar."

        show ana home happy
        a "Aprovado."

        h "Espero que você tenha gostado de jogos de ritmo. É um dos meus tipos favoritos porque fica difícil muito rápido."
    else:
        # If the player has not already seen the Jorge e Mateus DDR minigame.
        a "O que???? Sério? Onde? Quando? Eu não vi isso!"

        h "É um dos minigames, tente achar."

        h "Espero que você goste de jogos de ritmo. É um dos meus tipos favoritos porque fica difícil muito rápido."

        a "Como assim é bom porque fica difícil? Não é pra ser o contrário?"

        h "Se fosse fácil não teria graça."

        a "Maluco."

    # End of branching for Jorge e Mateus DDR minigame.

    h "E os mosaicos com nossas fotos? Gostou?" 

    if photo_gift_completed or "Fazer um presente caprichado com fotos" in inventory:
        # If the player has already chosen the mosaic gift and played the minigame, this line will be shown instead.
        a "Amei! São as mesmas fotos da minha capinha de celular."

        h "Que coincidência, não é?"

        a "Ah para."
    else:
        # If the player has not yet chosen the mosaic gift and played the minigame, this line will be shown.
        a "Mosaicos? Que mosaicos?"

        h "Caramba, tente me dar mais presentes."

    # End of branching for mosaic gift and minigame.

    a "Mas e nossas aventuras na França?"

    h "Bem, isso fica pra um próximo presente. Sem tempo irmão."

    h "Feliz aniversário, Ana."

    h "Essa versão ainda deixa espaço para a gente escrever o resto. Talvez um dia com os dois POVs completos para tudo."

    h "Mas por enquanto, essa parte é minha:"

    h "Eu amo você. Na Poli, no Crossing, na Supélec, em Aachen, em qualquer fuso horário e em qualquer ramo que a vida abrir."

    show ana home emotional

    scene black
    with fade

    $ unlock_achievement("birthday_complete")
    system_line "A vida continua."

    $ special_day_label = ""
    if endgame_replay_mode:
        return
    jump endgame_loop
    return
