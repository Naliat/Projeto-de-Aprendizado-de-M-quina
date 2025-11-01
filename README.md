# 🌍 Classificador de Planetas com Visão Computacional

Este projeto usa redes neurais convolucionais (CNNs) para classificar imagens de planetas do Sistema Solar.

## Estrutura
- `dataset/`: imagens organizadas por planeta
- `notebooks/train_model.ipynb`: notebook com o treinamento do modelo
- `model/planet_model.h5`: modelo treinado
- `app/app.py`: interface web com Streamlit

## Como usar
1. Instale as dependências
2. Execute o notebook para treinar o modelo
3. Rode a interface com `streamlit run app/app.py`

## 🔧 Melhorias no Modelo

Embora o classificador apresente boa precisão, ainda há espaço para aprimoramento. A qualidade e diversidade das imagens de entrada têm impacto direto na performance do modelo. Para torná-lo mais robusto e confiável, recomendamos:

- **Usar imagens mais variadas**: diferentes ângulos, estilos visuais e resoluções ajudam o modelo a aprender melhor os traços únicos de cada planeta.
- **Evitar imagens artificiais ou estilizadas** que possam confundir o modelo.
- **Aplicar técnicas de data augmentation** (rotação, zoom, inversão, ajuste de brilho) para aumentar a diversidade do conjunto de dados.
- **Balancear o número de imagens por classe** para evitar viés em planetas com mais exemplos.

Essas melhorias ajudam a reduzir confusões entre planetas visualmente semelhantes (como Júpiter e Marte) e aumentam a capacidade de generalização do modelo em cenários reais.


