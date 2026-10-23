# Assistente de voz

> Estado: ⚪ fase 2 · [← painel do hardware](README.md)

O assistente fala com o motorista dentro do quarto. O assistente é um extra. O quarto funciona completo sem ele. O trabalho começa depois da parte elétrica.

## O que o assistente faz

1. Alguns segundos depois da entrada do motorista, o assistente dá as boas-vindas.
2. O assistente explica o funcionamento do quarto.
3. O assistente informa o banho, o contrato e as regras.

## Direção proposta

Um satélite de voz por quarto, separado da parte elétrica → [ADR 0001](../ADRs/0001-central-zigbee-por-local.md).

- O satélite é um ESP32-S3 com microfone e alto-falante, ligado por Wi-Fi.
- A wake word roda no satélite (microWakeWord). O áudio só sai do quarto depois da wake word.
- A central do local faz o STT (faster_whisper) e o TTS (Kokoro).
- As falas fixas, como as boas-vindas, ficam em cache na central.
- O gatilho das boas-vindas está a definir, porque o quarto não tem sensor de porta. Esta fala não precisa de wake word.

| Candidato | Rede | O que tem | Preço |
|---|---|---|---|
| M5Stack Atom VoiceS3R | Wi-Fi | ESP32-S3, microfone, alto-falante de 1 W, emissor IR | a confirmar |
| FutureProofHomes Satellite1 | Wi-Fi | ESP32-S3 + XMOS, 4 microfones | cerca de US$ 80 no lançamento (2025) |
| Montagem própria | Wi-Fi | ESP32-S3 + INMP441 + MAX98357A | baixo em peças, alto em montagem |

## Perguntas

1. O assistente só fala, ou também recebe comandos de voz?
2. Quantos disparos falsos acontecem numa noite com o ar-condicionado ligado? Um disparo falso acorda o motorista.
3. O microfone precisa de botão físico de mudo e de LED? O quarto é de dormir, e o áudio é dado pessoal (LGPD).
4. A wake word "ei px" funciona no microWakeWord? O modelo atual é para o openWakeWord e precisa de um novo treino.
5. O alto-falante de 1 W é claro o suficiente para a fala do Kokoro em pt-BR?
6. O satélite de voz usa Wi-Fi em 2,4 GHz. Isso afeta o Zigbee → [hub-automacao.md](hub-automacao.md#coexistência-com-o-wi-fi).

## Ligação com o resto do sistema

- O gatilho das boas-vindas vem da central → [hub-automacao.md](hub-automacao.md).
- As informações do banho vêm do controle do banheiro → [banheiro.md](banheiro.md).
