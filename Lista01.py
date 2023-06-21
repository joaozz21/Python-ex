{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO2iNsFF6+Pe4ZKRa4BOU53",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/joaozz21/Python-ex/blob/main/Lista01.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "1.  Escreva um programa que ajude uma loja a fazer uma venda cujo pagamento  e parcelado. Assuma que a loja divide o preco em 19 parcelas iguais e sem quaisquer acrescimos (juros, multas, etc). Faca um programa que:\n",
        "- leia do teclado o preco do produto;\n",
        "- imprima quanto custara cada parcela (arredondando com duas casas decimais).\n",
        "- Veja aqui um exemplo:\n",
        "\n",
        "  ## Entrada:\n",
        "  665.95\n",
        "  ## Saida:\n",
        "  35.05"
      ],
      "metadata": {
        "id": "JVk2DULb83AZ"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 18,
      "metadata": {
        "id": "G5Its8iPIxi9",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "01cae2c6-9b0a-446c-88b0-cbdaa587781f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3.600\n",
            "3.300\n",
            "1.6498744056784245\n"
          ]
        }
      ],
      "source": [
        "preco=float(input())\n",
        "parcelas=preco/19\n",
        "print(f'{parcelas:.2f}')"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2.  Escreva um programa para ler (do teclado) dois numeros e somar o primeiro pelo segundo.\n",
        "Mostrar o resultado com duas casas decimais.\n",
        "\n",
        "  Veja aqui um exemplo:\n",
        "  ## Entradas:\n",
        "  41\n",
        "  ## Saida:Resultado =\n",
        "  5.00"
      ],
      "metadata": {
        "id": "BenlwNQk-Qzg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "num1=float(input())\n",
        "num2=float(input())\n",
        "soma=num1+num2\n",
        "print(f'Resultado = {soma:.2f}')"
      ],
      "metadata": {
        "id": "GYpADYvP-2_y"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "3.  Faca um programa contendo instrucoes para ler do teclado um numero inteiro que representa uma quantidade x de segundos. O programa deve imprimir na tela o numero de horas, minutos e segundos contidos em x no formato HH:MM:SS. Por exemplo, se x= 5000, entao o resultado devera ser 01:23:20, uma vez que 5000 segundos correspondem a 1 hora, 23 minutos e 20segundos.  Se x= 3600, o resultado devera ser 01:00:00(exatamente uma hora).\n",
        "Um exemplo e mostrado a seguir.\n",
        "  ## Entrada lida com o comando input:\n",
        "  3600\n",
        "  ## Saida correspondente a entrada:\n",
        "  01:00:00"
      ],
      "metadata": {
        "id": "xFRgWCUB-_y1"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "x=int(input())\n",
        "s= x%60\n",
        "m= (x//60)%60\n",
        "h= x//3600\n",
        "print(f\"{h:02d}:{m:02d}:{s:02d}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xoEAIpq9_w6r",
        "outputId": "b857125a-4444-4592-ce36-a0f2ad9ff0d1"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "7200\n",
            "02:00:00\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "4.  Faca um programa para calcular e imprimir o valor da expressao (formula) abaixo, a partir das variaveis reais A e B.  As variaveis A e B devem ser lidas do teclado, nessa ordem.\n",
        "\n",
        "   G=1−exp(−A/B)/2∗B\n",
        "\n",
        "   Mostrar o resultado, com tres casas decimais, conforme exemplo a seguir:\n",
        "\n",
        "   ## Entradas:\n",
        "   3.600\n",
        "\n",
        "   3.300\n",
        "   ## Saida:\n",
        "   G = 0.101"
      ],
      "metadata": {
        "id": "vLjxC9ANE-N5"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import math\n",
        "\n",
        "A=float(input())\n",
        "B=float(input())\n",
        "G=(1-math.exp(-A/B))/(2*B)\n",
        "\n",
        "print(f\"G = {G:.3f}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZZeyyyD6GoPV",
        "outputId": "261ff8ed-64c5-4882-8a46-23c6693b1018"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3.600\n",
            "3.300\n",
            "G = 0.101\n"
          ]
        }
      ]
    }
  ]
}