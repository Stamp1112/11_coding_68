{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPXopJe0wN70qC/NaKHHb+a",
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
        "<a href=\"https://colab.research.google.com/github/Stamp1112/11_coding_68/blob/main/mid-11-stamp.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KarQ7EfRvzat",
        "outputId": "8797259c-1651-435e-e48c-28acc04aa97a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ระดับแบตเตอรี่(%): 18\n",
            "กรุณาเสียบสายชาร์จ\n"
          ]
        }
      ],
      "source": [
        "แบตเตอรี่ = int(input(\"ระดับแบตเตอรี่(%): \"))\n",
        "if แบตเตอรี่ < 20 :\n",
        "    print(\"กรุณาเสียบสายชาร์จ\")\n",
        "else :\n",
        "    print(\"แบตเตอรี่อยู่ในระดับปกติ\")\n"
      ]
    }
  ]
}