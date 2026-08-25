{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "dKphWQXiE5gG"
      },
      "outputs": [],
      "source": [
        "# IMPORTACIÓN DE LIBRERIAS\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import re"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5-X9-qyOm1Cp",
        "outputId": "c0c93b7b-4885-4431-b160-d3e369d701fc"
      },
      "outputs": [],
      "source": [
        "#drive.mount(('/content/drive'), force_remount=True)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "9z1nKJ9Vnmmu"
      },
      "outputs": [],
      "source": [
        "# CARGA DE DATOS\n",
        "ruta_cl_online=\"clientes_online.csv\"\n",
        "ruta_cl_offline=\"clientes_offline.xlsx\"\n",
        "ruta_variable_demo=\"variables_crediticias_demografica.csv\"\n",
        "ruta_variable_laboral=\"variables_crediticias_laboral.xlsx\"\n",
        "ruta_prestamos=\"prestamos.csv\""
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "id": "cYnk6bAmorum"
      },
      "outputs": [],
      "source": [
        "df_cl_online=pd.read_csv(ruta_cl_online)\n",
        "df_cl_offline=pd.read_excel(ruta_cl_offline)\n",
        "df_demo=pd.read_csv(ruta_variable_demo)\n",
        "df_laboral=pd.read_excel(ruta_variable_laboral)\n",
        "df_prestamos=pd.read_csv(ruta_prestamos)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 667
        },
        "id": "aeYdnkD4qr-2",
        "outputId": "e232fb62-e1b8-4af8-9ef0-c55fca8996c4"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<class 'pandas.DataFrame'>\n",
            "RangeIndex: 7102 entries, 0 to 7101\n",
            "Data columns (total 7 columns):\n",
            " #   Column            Non-Null Count  Dtype\n",
            "---  ------            --------------  -----\n",
            " 0   id_cliente        7102 non-null   int64\n",
            " 1   nombre            7102 non-null   str  \n",
            " 2   apellido          6997 non-null   str  \n",
            " 3   fecha_nacimiento  7102 non-null   str  \n",
            " 4   fecha_alta        7102 non-null   str  \n",
            " 5   segmento          6995 non-null   str  \n",
            " 6   sucursal          7102 non-null   str  \n",
            "dtypes: int64(1), str(6)\n",
            "memory usage: 388.5 KB\n"
          ]
        },
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>id_cliente</th>\n",
              "      <th>nombre</th>\n",
              "      <th>apellido</th>\n",
              "      <th>fecha_nacimiento</th>\n",
              "      <th>fecha_alta</th>\n",
              "      <th>segmento</th>\n",
              "      <th>sucursal</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>7682</td>\n",
              "      <td>Federico</td>\n",
              "      <td>Rodríguez</td>\n",
              "      <td>28/08/1960</td>\n",
              "      <td>22/01/2023</td>\n",
              "      <td>tradicional</td>\n",
              "      <td>Casa Matriz</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>6737</td>\n",
              "      <td>Diego</td>\n",
              "      <td>González</td>\n",
              "      <td>26/06/1955</td>\n",
              "      <td>2021-12-02</td>\n",
              "      <td>emprendedor</td>\n",
              "      <td>Sucursal Norte</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>5517</td>\n",
              "      <td>Nicolás</td>\n",
              "      <td>López</td>\n",
              "      <td>1981-02-07</td>\n",
              "      <td>2023-12-14</td>\n",
              "      <td>PREMIUM</td>\n",
              "      <td>Sucursal Norte</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>735</td>\n",
              "      <td>Sofía</td>\n",
              "      <td>Martínez</td>\n",
              "      <td>1973-03-03</td>\n",
              "      <td>2023-02-06</td>\n",
              "      <td>tradicional</td>\n",
              "      <td>Sucursal Norte</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>3296</td>\n",
              "      <td>Tomás</td>\n",
              "      <td>García</td>\n",
              "      <td>1972-06-21</td>\n",
              "      <td>2021-11-13</td>\n",
              "      <td>emprendedor</td>\n",
              "      <td>Sucursal Sur</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7097</th>\n",
              "      <td>7060</td>\n",
              "      <td>Camila</td>\n",
              "      <td>López</td>\n",
              "      <td>29/10/1984</td>\n",
              "      <td>2021-02-04</td>\n",
              "      <td>emprendedor</td>\n",
              "      <td>Sucursal Sur</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7098</th>\n",
              "      <td>4676</td>\n",
              "      <td>Diego</td>\n",
              "      <td>Pérez</td>\n",
              "      <td>1980-09-29</td>\n",
              "      <td>2022-11-21</td>\n",
              "      <td>tradicional</td>\n",
              "      <td>Sucursal Centro</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7099</th>\n",
              "      <td>2354</td>\n",
              "      <td>Camila</td>\n",
              "      <td>Romero</td>\n",
              "      <td>1976-04-03</td>\n",
              "      <td>2023-01-22</td>\n",
              "      <td>premium</td>\n",
              "      <td>Sucursal Sur</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7100</th>\n",
              "      <td>3738</td>\n",
              "      <td>Nicolás</td>\n",
              "      <td>Sánchez</td>\n",
              "      <td>1963-08-02</td>\n",
              "      <td>2021-03-06</td>\n",
              "      <td>tradicional</td>\n",
              "      <td>Sucursal Centro</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7101</th>\n",
              "      <td>3917</td>\n",
              "      <td>Lucía</td>\n",
              "      <td>Fernández</td>\n",
              "      <td>1964-10-11</td>\n",
              "      <td>2021-11-03</td>\n",
              "      <td>tradicional</td>\n",
              "      <td>Sucursal Norte</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>7102 rows × 7 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "      id_cliente    nombre   apellido fecha_nacimiento  fecha_alta  \\\n",
              "0           7682  Federico  Rodríguez       28/08/1960  22/01/2023   \n",
              "1           6737     Diego   González       26/06/1955  2021-12-02   \n",
              "2           5517   Nicolás      López       1981-02-07  2023-12-14   \n",
              "3            735     Sofía   Martínez       1973-03-03  2023-02-06   \n",
              "4           3296     Tomás     García       1972-06-21  2021-11-13   \n",
              "...          ...       ...        ...              ...         ...   \n",
              "7097        7060    Camila      López       29/10/1984  2021-02-04   \n",
              "7098        4676     Diego      Pérez       1980-09-29  2022-11-21   \n",
              "7099        2354    Camila     Romero       1976-04-03  2023-01-22   \n",
              "7100        3738   Nicolás    Sánchez       1963-08-02  2021-03-06   \n",
              "7101        3917     Lucía  Fernández       1964-10-11  2021-11-03   \n",
              "\n",
              "         segmento         sucursal  \n",
              "0     tradicional      Casa Matriz  \n",
              "1     emprendedor   Sucursal Norte  \n",
              "2         PREMIUM   Sucursal Norte  \n",
              "3     tradicional   Sucursal Norte  \n",
              "4     emprendedor     Sucursal Sur  \n",
              "...           ...              ...  \n",
              "7097  emprendedor     Sucursal Sur  \n",
              "7098  tradicional  Sucursal Centro  \n",
              "7099      premium     Sucursal Sur  \n",
              "7100  tradicional  Sucursal Centro  \n",
              "7101  tradicional   Sucursal Norte  \n",
              "\n",
              "[7102 rows x 7 columns]"
            ]
          },
          "execution_count": 5,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "#XPLORACION INICIAL\n",
        "df_cl_offline.info()\n",
        "df_cl_offline"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 667
        },
        "id": "_vEfyw4Mq-Hw",
        "outputId": "b0a2da06-f2cf-4e07-8946-b9269573e43b"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<class 'pandas.DataFrame'>\n",
            "RangeIndex: 5538 entries, 0 to 5537\n",
            "Data columns (total 7 columns):\n",
            " #   Column               Non-Null Count  Dtype\n",
            "---  ------               --------------  -----\n",
            " 0   customer_id          5538 non-null   int64\n",
            " 1   first_name           5538 non-null   str  \n",
            " 2   last_name            5455 non-null   str  \n",
            " 3   birth_date           5538 non-null   str  \n",
            " 4   signup_date          5538 non-null   str  \n",
            " 5   segment              5456 non-null   str  \n",
            " 6   acquisition_channel  5538 non-null   str  \n",
            "dtypes: int64(1), str(6)\n",
            "memory usage: 303.0 KB\n"
          ]
        },
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>customer_id</th>\n",
              "      <th>first_name</th>\n",
              "      <th>last_name</th>\n",
              "      <th>birth_date</th>\n",
              "      <th>signup_date</th>\n",
              "      <th>segment</th>\n",
              "      <th>acquisition_channel</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>3378</td>\n",
              "      <td>Julieta</td>\n",
              "      <td>González</td>\n",
              "      <td>1984-10-12T00:00:00</td>\n",
              "      <td>2022-07-13</td>\n",
              "      <td>traditional</td>\n",
              "      <td>app</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>6959</td>\n",
              "      <td>Valentina</td>\n",
              "      <td>Díaz</td>\n",
              "      <td>1963-03-21T00:00:00</td>\n",
              "      <td>2021-08-30</td>\n",
              "      <td>premium</td>\n",
              "      <td>web</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>6425</td>\n",
              "      <td>Bruno</td>\n",
              "      <td>Díaz</td>\n",
              "      <td>1992-04-12T00:00:00</td>\n",
              "      <td>2022-10-03</td>\n",
              "      <td>entrepreneur</td>\n",
              "      <td>web</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>9611</td>\n",
              "      <td>Bruno</td>\n",
              "      <td>Rodríguez</td>\n",
              "      <td>1971-08-27T00:00:00</td>\n",
              "      <td>2023-09-16</td>\n",
              "      <td>TRADITIONAL</td>\n",
              "      <td>web</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>4016</td>\n",
              "      <td>Martín</td>\n",
              "      <td>García</td>\n",
              "      <td>2000-05-13T00:00:00</td>\n",
              "      <td>2022-05-31</td>\n",
              "      <td>Premium</td>\n",
              "      <td>app</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5533</th>\n",
              "      <td>1661</td>\n",
              "      <td>Julieta</td>\n",
              "      <td>Martínez</td>\n",
              "      <td>1957-03-29T00:00:00</td>\n",
              "      <td>2022-10-11</td>\n",
              "      <td>entrepreneur</td>\n",
              "      <td>app</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5534</th>\n",
              "      <td>9535</td>\n",
              "      <td>Martín</td>\n",
              "      <td>Torres</td>\n",
              "      <td>2003-01-01T00:00:00</td>\n",
              "      <td>2023-03-13</td>\n",
              "      <td>premium</td>\n",
              "      <td>referral</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5535</th>\n",
              "      <td>7279</td>\n",
              "      <td>Nicolás</td>\n",
              "      <td>Rodríguez</td>\n",
              "      <td>1980-05-31T00:00:00</td>\n",
              "      <td>2023-04-07</td>\n",
              "      <td>traditional</td>\n",
              "      <td>app</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5536</th>\n",
              "      <td>459</td>\n",
              "      <td>Tomás</td>\n",
              "      <td>Fernández</td>\n",
              "      <td>1960-03-09T00:00:00</td>\n",
              "      <td>2022-02-02</td>\n",
              "      <td>entrepreneur</td>\n",
              "      <td>app</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5537</th>\n",
              "      <td>9473</td>\n",
              "      <td>Agustina</td>\n",
              "      <td>Sánchez</td>\n",
              "      <td>1959-04-29T00:00:00</td>\n",
              "      <td>2023-11-18</td>\n",
              "      <td>traditional</td>\n",
              "      <td>referral</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>5538 rows × 7 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "      customer_id first_name  last_name           birth_date signup_date  \\\n",
              "0            3378    Julieta   González  1984-10-12T00:00:00  2022-07-13   \n",
              "1            6959  Valentina       Díaz  1963-03-21T00:00:00  2021-08-30   \n",
              "2            6425      Bruno       Díaz  1992-04-12T00:00:00  2022-10-03   \n",
              "3            9611      Bruno  Rodríguez  1971-08-27T00:00:00  2023-09-16   \n",
              "4            4016     Martín     García  2000-05-13T00:00:00  2022-05-31   \n",
              "...           ...        ...        ...                  ...         ...   \n",
              "5533         1661    Julieta   Martínez  1957-03-29T00:00:00  2022-10-11   \n",
              "5534         9535     Martín     Torres  2003-01-01T00:00:00  2023-03-13   \n",
              "5535         7279    Nicolás  Rodríguez  1980-05-31T00:00:00  2023-04-07   \n",
              "5536          459      Tomás  Fernández  1960-03-09T00:00:00  2022-02-02   \n",
              "5537         9473   Agustina    Sánchez  1959-04-29T00:00:00  2023-11-18   \n",
              "\n",
              "           segment acquisition_channel  \n",
              "0      traditional                 app  \n",
              "1          premium                 web  \n",
              "2     entrepreneur                 web  \n",
              "3      TRADITIONAL                 web  \n",
              "4          Premium                 app  \n",
              "...            ...                 ...  \n",
              "5533  entrepreneur                 app  \n",
              "5534       premium            referral  \n",
              "5535   traditional                 app  \n",
              "5536  entrepreneur                 app  \n",
              "5537   traditional            referral  \n",
              "\n",
              "[5538 rows x 7 columns]"
            ]
          },
          "execution_count": 6,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df_cl_online.info()\n",
        "df_cl_online"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 649
        },
        "id": "pj0gkXzpsHzq",
        "outputId": "880b650b-3f34-4997-a2c1-6bbc661b717d"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<class 'pandas.DataFrame'>\n",
            "RangeIndex: 6696 entries, 0 to 6695\n",
            "Data columns (total 6 columns):\n",
            " #   Column              Non-Null Count  Dtype  \n",
            "---  ------              --------------  -----  \n",
            " 0   id_prestamo         6696 non-null   int64  \n",
            " 1   id_cliente          6696 non-null   int64  \n",
            " 2   fecha_otorgamiento  6696 non-null   str    \n",
            " 3   monto               6696 non-null   str    \n",
            " 4   tasa_interes        6629 non-null   float64\n",
            " 5   cantidad_cuotas     6696 non-null   int64  \n",
            "dtypes: float64(1), int64(3), str(2)\n",
            "memory usage: 314.0 KB\n"
          ]
        },
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>id_prestamo</th>\n",
              "      <th>id_cliente</th>\n",
              "      <th>fecha_otorgamiento</th>\n",
              "      <th>monto</th>\n",
              "      <th>tasa_interes</th>\n",
              "      <th>cantidad_cuotas</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>5505</td>\n",
              "      <td>8429</td>\n",
              "      <td>2024-05-06</td>\n",
              "      <td>673310.04</td>\n",
              "      <td>54.36</td>\n",
              "      <td>6</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>274</td>\n",
              "      <td>417</td>\n",
              "      <td>2024-10-23</td>\n",
              "      <td>386.388,21</td>\n",
              "      <td>52.89</td>\n",
              "      <td>24</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3319</td>\n",
              "      <td>5083</td>\n",
              "      <td>2024-02-21</td>\n",
              "      <td>367122.70</td>\n",
              "      <td>61.94</td>\n",
              "      <td>18</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1761</td>\n",
              "      <td>2702</td>\n",
              "      <td>2024-01-19</td>\n",
              "      <td>201623.48</td>\n",
              "      <td>46.91</td>\n",
              "      <td>24</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1566</td>\n",
              "      <td>2408</td>\n",
              "      <td>2024-02-17</td>\n",
              "      <td>485006.50</td>\n",
              "      <td>51.04</td>\n",
              "      <td>6</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6691</th>\n",
              "      <td>6444</td>\n",
              "      <td>9834</td>\n",
              "      <td>2024-06-24</td>\n",
              "      <td>755.414,69</td>\n",
              "      <td>53.72</td>\n",
              "      <td>18</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6692</th>\n",
              "      <td>3607</td>\n",
              "      <td>5528</td>\n",
              "      <td>2024-07-06</td>\n",
              "      <td>228237.18</td>\n",
              "      <td>56.63</td>\n",
              "      <td>18</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6693</th>\n",
              "      <td>5705</td>\n",
              "      <td>8713</td>\n",
              "      <td>2024-01-10</td>\n",
              "      <td>1052877.47</td>\n",
              "      <td>60.66</td>\n",
              "      <td>12</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6694</th>\n",
              "      <td>4174</td>\n",
              "      <td>6436</td>\n",
              "      <td>2024-03-31</td>\n",
              "      <td>458.288,65</td>\n",
              "      <td>54.43</td>\n",
              "      <td>18</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6695</th>\n",
              "      <td>2576</td>\n",
              "      <td>3957</td>\n",
              "      <td>2023-10-12</td>\n",
              "      <td>466147.46</td>\n",
              "      <td>57.12</td>\n",
              "      <td>12</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>6696 rows × 6 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "      id_prestamo  id_cliente fecha_otorgamiento       monto  tasa_interes  \\\n",
              "0            5505        8429         2024-05-06   673310.04         54.36   \n",
              "1             274         417         2024-10-23  386.388,21         52.89   \n",
              "2            3319        5083         2024-02-21   367122.70         61.94   \n",
              "3            1761        2702         2024-01-19   201623.48         46.91   \n",
              "4            1566        2408         2024-02-17   485006.50         51.04   \n",
              "...           ...         ...                ...         ...           ...   \n",
              "6691         6444        9834         2024-06-24  755.414,69         53.72   \n",
              "6692         3607        5528         2024-07-06   228237.18         56.63   \n",
              "6693         5705        8713         2024-01-10  1052877.47         60.66   \n",
              "6694         4174        6436         2024-03-31  458.288,65         54.43   \n",
              "6695         2576        3957         2023-10-12   466147.46         57.12   \n",
              "\n",
              "      cantidad_cuotas  \n",
              "0                   6  \n",
              "1                  24  \n",
              "2                  18  \n",
              "3                  24  \n",
              "4                   6  \n",
              "...               ...  \n",
              "6691               18  \n",
              "6692               18  \n",
              "6693               12  \n",
              "6694               18  \n",
              "6695               12  \n",
              "\n",
              "[6696 rows x 6 columns]"
            ]
          },
          "execution_count": 7,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df_prestamos.info()\n",
        "df_prestamos"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 649
        },
        "id": "W4djwQpUsdua",
        "outputId": "53713165-c471-4b6c-fe17-a1816f1ca337"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<class 'pandas.DataFrame'>\n",
            "RangeIndex: 7984 entries, 0 to 7983\n",
            "Data columns (total 6 columns):\n",
            " #   Column                 Non-Null Count  Dtype\n",
            "---  ------                 --------------  -----\n",
            " 0   id_cliente             7984 non-null   int64\n",
            " 1   edad                   7984 non-null   int64\n",
            " 2   estado_civil           7984 non-null   str  \n",
            " 3   nivel_educativo        7905 non-null   str  \n",
            " 4   cantidad_dependientes  7984 non-null   int64\n",
            " 5   provincia              7984 non-null   str  \n",
            "dtypes: int64(3), str(3)\n",
            "memory usage: 374.4 KB\n"
          ]
        },
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>id_cliente</th>\n",
              "      <th>edad</th>\n",
              "      <th>estado_civil</th>\n",
              "      <th>nivel_educativo</th>\n",
              "      <th>cantidad_dependientes</th>\n",
              "      <th>provincia</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1227</td>\n",
              "      <td>64</td>\n",
              "      <td>divorciado</td>\n",
              "      <td>terciario</td>\n",
              "      <td>2</td>\n",
              "      <td>Tucumán</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>8617</td>\n",
              "      <td>30</td>\n",
              "      <td>soltero</td>\n",
              "      <td>universitario</td>\n",
              "      <td>1</td>\n",
              "      <td>buenos aires</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2405</td>\n",
              "      <td>28</td>\n",
              "      <td>soltero</td>\n",
              "      <td>universitario</td>\n",
              "      <td>0</td>\n",
              "      <td>Buenos Aires</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4206</td>\n",
              "      <td>49</td>\n",
              "      <td>soltero</td>\n",
              "      <td>universitario</td>\n",
              "      <td>0</td>\n",
              "      <td>Buenos Aires</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>7516</td>\n",
              "      <td>49</td>\n",
              "      <td>casado</td>\n",
              "      <td>secundario</td>\n",
              "      <td>3</td>\n",
              "      <td>Buenos Aires</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7979</th>\n",
              "      <td>7639</td>\n",
              "      <td>70</td>\n",
              "      <td>soltero</td>\n",
              "      <td>secundario</td>\n",
              "      <td>0</td>\n",
              "      <td>Santa Fe</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7980</th>\n",
              "      <td>932</td>\n",
              "      <td>27</td>\n",
              "      <td>soltero</td>\n",
              "      <td>terciario</td>\n",
              "      <td>1</td>\n",
              "      <td>Tucumán</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7981</th>\n",
              "      <td>3179</td>\n",
              "      <td>30</td>\n",
              "      <td>soltero</td>\n",
              "      <td>posgrado</td>\n",
              "      <td>1</td>\n",
              "      <td>Tucumán</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7982</th>\n",
              "      <td>229</td>\n",
              "      <td>48</td>\n",
              "      <td>soltero</td>\n",
              "      <td>posgrado</td>\n",
              "      <td>1</td>\n",
              "      <td>Buenos Aires</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7983</th>\n",
              "      <td>1483</td>\n",
              "      <td>24</td>\n",
              "      <td>casado</td>\n",
              "      <td>universitario</td>\n",
              "      <td>2</td>\n",
              "      <td>Buenos Aires</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>7984 rows × 6 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "      id_cliente  edad estado_civil nivel_educativo  cantidad_dependientes  \\\n",
              "0           1227    64   divorciado       terciario                      2   \n",
              "1           8617    30      soltero   universitario                      1   \n",
              "2           2405    28      soltero   universitario                      0   \n",
              "3           4206    49      soltero   universitario                      0   \n",
              "4           7516    49       casado      secundario                      3   \n",
              "...          ...   ...          ...             ...                    ...   \n",
              "7979        7639    70      soltero      secundario                      0   \n",
              "7980         932    27      soltero       terciario                      1   \n",
              "7981        3179    30      soltero        posgrado                      1   \n",
              "7982         229    48      soltero        posgrado                      1   \n",
              "7983        1483    24       casado   universitario                      2   \n",
              "\n",
              "         provincia  \n",
              "0          Tucumán  \n",
              "1     buenos aires  \n",
              "2     Buenos Aires  \n",
              "3     Buenos Aires  \n",
              "4     Buenos Aires  \n",
              "...            ...  \n",
              "7979      Santa Fe  \n",
              "7980       Tucumán  \n",
              "7981       Tucumán  \n",
              "7982  Buenos Aires  \n",
              "7983  Buenos Aires  \n",
              "\n",
              "[7984 rows x 6 columns]"
            ]
          },
          "execution_count": 8,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df_demo.info()\n",
        "df_demo"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 649
        },
        "id": "TaA4KqcdsyXM",
        "outputId": "109ee477-ae3e-4e65-b1b9-18f155163bc6"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<class 'pandas.DataFrame'>\n",
            "RangeIndex: 7596 entries, 0 to 7595\n",
            "Data columns (total 6 columns):\n",
            " #   Column                    Non-Null Count  Dtype  \n",
            "---  ------                    --------------  -----  \n",
            " 0   id_cliente                7596 non-null   int64  \n",
            " 1   ingreso_mensual           7596 non-null   str    \n",
            " 2   antiguedad_laboral_anios  7596 non-null   float64\n",
            " 3   situacion_laboral         7596 non-null   str    \n",
            " 4   atrasos_historicos_12m    7481 non-null   float64\n",
            " 5   ratio_endeudamiento       7596 non-null   float64\n",
            "dtypes: float64(3), int64(1), str(2)\n",
            "memory usage: 356.2 KB\n"
          ]
        },
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>id_cliente</th>\n",
              "      <th>ingreso_mensual</th>\n",
              "      <th>antiguedad_laboral_anios</th>\n",
              "      <th>situacion_laboral</th>\n",
              "      <th>atrasos_historicos_12m</th>\n",
              "      <th>ratio_endeudamiento</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>56</td>\n",
              "      <td>302.850,00</td>\n",
              "      <td>3.96</td>\n",
              "      <td>empleado</td>\n",
              "      <td>3.0</td>\n",
              "      <td>0.329</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1521</td>\n",
              "      <td>192907.00</td>\n",
              "      <td>9.16</td>\n",
              "      <td>empleado</td>\n",
              "      <td>2.0</td>\n",
              "      <td>0.537</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>7659</td>\n",
              "      <td>187.176,00</td>\n",
              "      <td>1.83</td>\n",
              "      <td>empleado</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.398</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>9784</td>\n",
              "      <td>40000.00</td>\n",
              "      <td>4.66</td>\n",
              "      <td>empleado</td>\n",
              "      <td>2.0</td>\n",
              "      <td>0.271</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>2875</td>\n",
              "      <td>153.096,00</td>\n",
              "      <td>5.55</td>\n",
              "      <td>empleado</td>\n",
              "      <td>2.0</td>\n",
              "      <td>0.655</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7591</th>\n",
              "      <td>9434</td>\n",
              "      <td>194.834,00</td>\n",
              "      <td>9.43</td>\n",
              "      <td>empleado</td>\n",
              "      <td>2.0</td>\n",
              "      <td>0.399</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7592</th>\n",
              "      <td>2232</td>\n",
              "      <td>232315.00</td>\n",
              "      <td>4.63</td>\n",
              "      <td>monotributista</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.284</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7593</th>\n",
              "      <td>4434</td>\n",
              "      <td>182812.00</td>\n",
              "      <td>5.49</td>\n",
              "      <td>independiente</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.219</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7594</th>\n",
              "      <td>2265</td>\n",
              "      <td>124.077,00</td>\n",
              "      <td>5.03</td>\n",
              "      <td>independiente</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.448</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7595</th>\n",
              "      <td>7985</td>\n",
              "      <td>215.765,00</td>\n",
              "      <td>0.61</td>\n",
              "      <td>empleado</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.303</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>7596 rows × 6 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "      id_cliente ingreso_mensual  antiguedad_laboral_anios situacion_laboral  \\\n",
              "0             56      302.850,00                      3.96          empleado   \n",
              "1           1521       192907.00                      9.16          empleado   \n",
              "2           7659      187.176,00                      1.83          empleado   \n",
              "3           9784        40000.00                      4.66          empleado   \n",
              "4           2875      153.096,00                      5.55          empleado   \n",
              "...          ...             ...                       ...               ...   \n",
              "7591        9434      194.834,00                      9.43          empleado   \n",
              "7592        2232       232315.00                      4.63    monotributista   \n",
              "7593        4434       182812.00                      5.49     independiente   \n",
              "7594        2265      124.077,00                      5.03     independiente   \n",
              "7595        7985      215.765,00                      0.61          empleado   \n",
              "\n",
              "      atrasos_historicos_12m  ratio_endeudamiento  \n",
              "0                        3.0                0.329  \n",
              "1                        2.0                0.537  \n",
              "2                        1.0                0.398  \n",
              "3                        2.0                0.271  \n",
              "4                        2.0                0.655  \n",
              "...                      ...                  ...  \n",
              "7591                     2.0                0.399  \n",
              "7592                     0.0                0.284  \n",
              "7593                     0.0                0.219  \n",
              "7594                     0.0                0.448  \n",
              "7595                     0.0                0.303  \n",
              "\n",
              "[7596 rows x 6 columns]"
            ]
          },
          "execution_count": 9,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df_laboral.info()\n",
        "df_laboral"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 304
        },
        "id": "O9IAwIsA0_EE",
        "outputId": "9b6d6c86-1289-4805-d278-5d29430eaee3"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "id_cliente            0\n",
              "nombre                0\n",
              "apellido            105\n",
              "fecha_nacimiento      0\n",
              "fecha_alta            0\n",
              "segmento            107\n",
              "sucursal              0\n",
              "dtype: int64"
            ]
          },
          "execution_count": 10,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df_cl_offline.isna().sum()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 304
        },
        "id": "kHT1XwJq1HQM",
        "outputId": "d0451741-5de8-48ed-e988-d9840c9afb9e"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "customer_id             0\n",
              "first_name              0\n",
              "last_name              83\n",
              "birth_date              0\n",
              "signup_date             0\n",
              "segment                82\n",
              "acquisition_channel     0\n",
              "dtype: int64"
            ]
          },
          "execution_count": 11,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df_cl_online.isna().sum()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 272
        },
        "id": "V2DFtF4L1OV_",
        "outputId": "9ebb8a8a-5095-4b71-da83-2a8db4fcc4b2"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "id_cliente                0\n",
              "edad                      0\n",
              "estado_civil              0\n",
              "nivel_educativo          79\n",
              "cantidad_dependientes     0\n",
              "provincia                 0\n",
              "dtype: int64"
            ]
          },
          "execution_count": 12,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df_demo.isna().sum()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 272
        },
        "id": "ZLfIcz4w1nCS",
        "outputId": "90ac869c-1fc6-49d4-e881-cd740c78fde1"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "id_cliente                    0\n",
              "ingreso_mensual               0\n",
              "antiguedad_laboral_anios      0\n",
              "situacion_laboral             0\n",
              "atrasos_historicos_12m      115\n",
              "ratio_endeudamiento           0\n",
              "dtype: int64"
            ]
          },
          "execution_count": 13,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df_laboral.isna().sum()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 272
        },
        "id": "gPsTDgsp1sAA",
        "outputId": "279a0c1d-c2bc-44bd-cce9-0ec8363a86a7"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "id_prestamo            0\n",
              "id_cliente             0\n",
              "fecha_otorgamiento     0\n",
              "monto                  0\n",
              "tasa_interes          67\n",
              "cantidad_cuotas        0\n",
              "dtype: int64"
            ]
          },
          "execution_count": 14,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df_prestamos.isna().sum()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 304
        },
        "id": "tgzWRKpV164c",
        "outputId": "ea653fae-a1cc-4118-b8d3-53b60d1c7b50"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "id_cliente          6963\n",
              "nombre                14\n",
              "apellido              12\n",
              "fecha_nacimiento    6245\n",
              "fecha_alta          1969\n",
              "segmento               9\n",
              "sucursal               4\n",
              "dtype: int64"
            ]
          },
          "execution_count": 15,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df_cl_offline.nunique()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 304
        },
        "id": "4ZAE8n4C2FwH",
        "outputId": "7994bbbf-f247-4092-8ffe-e9515a22f2e4"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "customer_id            5456\n",
              "first_name               14\n",
              "last_name                12\n",
              "birth_date             4729\n",
              "signup_date            1080\n",
              "segment                   9\n",
              "acquisition_channel       3\n",
              "dtype: int64"
            ]
          },
          "execution_count": 16,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df_cl_online.nunique()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 17,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 272
        },
        "id": "Q5anZ6ut2LFm",
        "outputId": "b1949788-0354-49d4-cf8b-80f86b979a1f"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "id_prestamo           6598\n",
              "id_cliente            6598\n",
              "fecha_otorgamiento     457\n",
              "monto                 6465\n",
              "tasa_interes          2180\n",
              "cantidad_cuotas          5\n",
              "dtype: int64"
            ]
          },
          "execution_count": 17,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df_prestamos.nunique()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 18,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 272
        },
        "id": "wP6ohnaj2Q3W",
        "outputId": "4686393d-5959-4f2a-e91b-188d00096581"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "id_cliente               7905\n",
              "edad                       51\n",
              "estado_civil                4\n",
              "nivel_educativo             4\n",
              "cantidad_dependientes       7\n",
              "provincia                   9\n",
              "dtype: int64"
            ]
          },
          "execution_count": 18,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df_demo.nunique()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 19,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 272
        },
        "id": "DEeZui_z2Yee",
        "outputId": "9be2a4bb-7f3c-41b4-a3ab-a821625c744a"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "id_cliente                  7521\n",
              "ingreso_mensual             7369\n",
              "antiguedad_laboral_anios    1468\n",
              "situacion_laboral              4\n",
              "atrasos_historicos_12m         7\n",
              "ratio_endeudamiento          744\n",
              "dtype: int64"
            ]
          },
          "execution_count": 19,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df_laboral.nunique()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 20,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f1bm6Ht56RvD",
        "outputId": "3e546de5-f8bf-40bc-f79e-0d9add0e0506"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "offline: 28 filas duplicadas exactas\n",
            "online: 82 filas duplicadas exactas\n",
            "prestamos: 98 filas duplicadas exactas\n",
            "demo: 79 filas duplicadas exactas\n",
            "laboral: 75 filas duplicadas exactas\n"
          ]
        }
      ],
      "source": [
        "for nombre, df, key in [\n",
        "    ('offline', df_cl_offline, 'id_cliente'),\n",
        "    ('online', df_cl_online, 'customer_id'),\n",
        "    ('prestamos', df_prestamos, 'id_prestamo'),\n",
        "    ('demo', df_demo, 'id_cliente'),\n",
        "    ('laboral', df_laboral, 'id_cliente'),\n",
        "]:\n",
        "    exactos = df.duplicated().sum()\n",
        "    print(f\"{nombre}: {exactos} filas duplicadas exactas\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 21,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "THVPkFit66Ci",
        "outputId": "e2d3ff86-f9f2-4d97-c483-1916a01b1260"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "offline: 28 duplicados exactos eliminados (7102 -> 7074)\n",
            "online: 82 duplicados exactos eliminados (5538 -> 5456)\n",
            "prestamos: 98 duplicados exactos eliminados (6696 -> 6598)\n",
            "demo: 79 duplicados exactos eliminados (7984 -> 7905)\n",
            "laboral: 75 duplicados exactos eliminados (7596 -> 7521)\n"
          ]
        }
      ],
      "source": [
        "# ELIMINACIÓN DE DUPLICADOS EXACTOS\n",
        "dataframes = {\n",
        "    'offline': df_cl_offline,\n",
        "    'online': df_cl_online,\n",
        "    'prestamos': df_prestamos,\n",
        "    'demo': df_demo,\n",
        "    'laboral': df_laboral,\n",
        "}\n",
        "\n",
        "resumen_duplicados = {}\n",
        "for nombre, df in dataframes.items():\n",
        "    n_antes = len(df)\n",
        "    df.drop_duplicates(inplace=True)\n",
        "    n_despues = len(df)\n",
        "    resumen_duplicados[nombre] = n_antes - n_despues\n",
        "    print(f\"{nombre}: {n_antes - n_despues} duplicados exactos eliminados ({n_antes} -> {n_despues})\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 22,
      "metadata": {
        "id": "SqjvCY0r8U8C"
      },
      "outputs": [],
      "source": [
        "# NORMALIZACIÓN DE FECHAS\n",
        "def parsear_fecha_offline(valor):\n",
        "    valor = str(valor)\n",
        "    if '/' in valor:\n",
        "        # formato DD/MM/AAAA -> dayfirst=True\n",
        "        return pd.to_datetime(valor, format='%d/%m/%Y')\n",
        "    else:\n",
        "        # formato ISO AAAA-MM-DD -> sin ambigüedad\n",
        "        return pd.to_datetime(valor, format='%Y-%m-%d')\n",
        "\n",
        "df_cl_offline['fecha_nacimiento'] = df_cl_offline['fecha_nacimiento'].apply(parsear_fecha_offline)\n",
        "df_cl_offline['fecha_alta'] = df_cl_offline['fecha_alta'].apply(parsear_fecha_offline)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 23,
      "metadata": {},
      "outputs": [],
      "source": [
        "df_cl_online['birth_date'] = pd.to_datetime(df_cl_online['birth_date'], format='mixed')\n",
        "df_cl_online['signup_date'] = pd.to_datetime(df_cl_online['signup_date'], format='mixed')\n",
        "\n",
        "df_prestamos['fecha_otorgamiento'] = pd.to_datetime(df_prestamos['fecha_otorgamiento'], format='mixed')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 24,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 269
        },
        "id": "LqCKGwpC8YqI",
        "outputId": "0f9f91a1-023f-4e58-ae4f-067604245fc2"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>fecha_nacimiento</th>\n",
              "      <th>fecha_alta</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>7074</td>\n",
              "      <td>7074</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>1980-02-22 10:54:02.748091</td>\n",
              "      <td>2022-07-03 06:25:32.824427</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>1955-01-01 00:00:00</td>\n",
              "      <td>2021-01-01 00:00:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>1967-07-03 06:00:00</td>\n",
              "      <td>2021-09-27 00:00:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>1980-04-13 00:00:00</td>\n",
              "      <td>2022-07-08 00:00:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>1992-08-17 12:00:00</td>\n",
              "      <td>2023-04-05 00:00:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>2004-12-18 00:00:00</td>\n",
              "      <td>2023-12-31 00:00:00</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                 fecha_nacimiento                  fecha_alta\n",
              "count                        7074                        7074\n",
              "mean   1980-02-22 10:54:02.748091  2022-07-03 06:25:32.824427\n",
              "min           1955-01-01 00:00:00         2021-01-01 00:00:00\n",
              "25%           1967-07-03 06:00:00         2021-09-27 00:00:00\n",
              "50%           1980-04-13 00:00:00         2022-07-08 00:00:00\n",
              "75%           1992-08-17 12:00:00         2023-04-05 00:00:00\n",
              "max           2004-12-18 00:00:00         2023-12-31 00:00:00"
            ]
          },
          "execution_count": 24,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df_cl_offline[['fecha_nacimiento', 'fecha_alta']].describe()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 25,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 269
        },
        "id": "KKB4j4508rjr",
        "outputId": "eb41456d-2ba6-4614-de77-ba05b90bfbd9"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>birth_date</th>\n",
              "      <th>signup_date</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>5456</td>\n",
              "      <td>5456</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>1980-02-16 22:35:48.387096</td>\n",
              "      <td>2022-07-03 01:04:08.093841</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>1955-01-01 00:00:00</td>\n",
              "      <td>2021-01-01 00:00:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>1967-07-14 12:00:00</td>\n",
              "      <td>2021-10-01 18:00:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>1980-03-09 00:00:00</td>\n",
              "      <td>2022-07-05 00:00:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>1992-08-24 12:00:00</td>\n",
              "      <td>2023-04-02 00:00:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>2004-12-18 00:00:00</td>\n",
              "      <td>2023-12-31 00:00:00</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                       birth_date                 signup_date\n",
              "count                        5456                        5456\n",
              "mean   1980-02-16 22:35:48.387096  2022-07-03 01:04:08.093841\n",
              "min           1955-01-01 00:00:00         2021-01-01 00:00:00\n",
              "25%           1967-07-14 12:00:00         2021-10-01 18:00:00\n",
              "50%           1980-03-09 00:00:00         2022-07-05 00:00:00\n",
              "75%           1992-08-24 12:00:00         2023-04-02 00:00:00\n",
              "max           2004-12-18 00:00:00         2023-12-31 00:00:00"
            ]
          },
          "execution_count": 25,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df_cl_online[['birth_date', 'signup_date']].describe()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 26,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 269
        },
        "id": "51k-8QSo8vnU",
        "outputId": "94afb78b-da97-4400-b774-a997ef42cb86"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>fecha_otorgamiento</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>6598</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>2024-05-26 11:22:40.775992</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>2023-10-01 00:00:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>2024-01-30 00:00:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>2024-06-02 00:00:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>2024-09-22 00:00:00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>2024-12-30 00:00:00</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "               fecha_otorgamiento\n",
              "count                        6598\n",
              "mean   2024-05-26 11:22:40.775992\n",
              "min           2023-10-01 00:00:00\n",
              "25%           2024-01-30 00:00:00\n",
              "50%           2024-06-02 00:00:00\n",
              "75%           2024-09-22 00:00:00\n",
              "max           2024-12-30 00:00:00"
            ]
          },
          "execution_count": 26,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "df_prestamos[['fecha_otorgamiento']].describe()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 27,
      "metadata": {
        "id": "y6VkcOgS99IN"
      },
      "outputs": [],
      "source": [
        "def normalizar_monto(valor):\n",
        "    valor = str(valor)\n",
        "    if ',' in valor:\n",
        "        # formato argentino: 386.388,21 -> sacar puntos, coma a punto - formato plano -> se convierte directo a número\n",
        "        valor = valor.replace('.', '').replace(',', '.')\n",
        "    return float(valor)\n",
        "\n",
        "df_prestamos['monto'] = df_prestamos['monto'].apply(normalizar_monto)\n",
        "df_laboral['ingreso_mensual'] = df_laboral['ingreso_mensual'].apply(normalizar_monto)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 28,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 578
        },
        "id": "P1VURkzH-QAQ",
        "outputId": "3e6d14f0-6502-4c08-e190-4b6885c86d21"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "float64\n",
            "0\n",
            "           monto\n",
            "0      673310.04\n",
            "1      386388.21\n",
            "2      367122.70\n",
            "3      201623.48\n",
            "4      485006.50\n",
            "...          ...\n",
            "6690   586999.30\n",
            "6691   755414.69\n",
            "6692   228237.18\n",
            "6693  1052877.47\n",
            "6695   466147.46\n",
            "\n",
            "[6598 rows x 1 columns]\n"
          ]
        },
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>monto</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>6.598000e+03</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>5.823106e+05</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>2.997649e+05</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>5.423755e+04</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>3.644986e+05</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>5.290220e+05</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>7.447432e+05</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>1.500000e+06</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "              monto\n",
              "count  6.598000e+03\n",
              "mean   5.823106e+05\n",
              "std    2.997649e+05\n",
              "min    5.423755e+04\n",
              "25%    3.644986e+05\n",
              "50%    5.290220e+05\n",
              "75%    7.447432e+05\n",
              "max    1.500000e+06"
            ]
          },
          "execution_count": 28,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "print(df_prestamos['monto'].dtype)\n",
        "print(df_prestamos['monto'].isna().sum())\n",
        "print(df_prestamos[['monto']])\n",
        "df_prestamos[['monto']].describe()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 29,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 578
        },
        "id": "VVOtkTKK_DaR",
        "outputId": "531d606f-1c7e-4eec-8f0d-99fcacf15305"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "float64\n",
            "0\n",
            "      ingreso_mensual\n",
            "0            302850.0\n",
            "1            192907.0\n",
            "2            187176.0\n",
            "3             40000.0\n",
            "4            153096.0\n",
            "...               ...\n",
            "7591         194834.0\n",
            "7592         232315.0\n",
            "7593         182812.0\n",
            "7594         124077.0\n",
            "7595         215765.0\n",
            "\n",
            "[7521 rows x 1 columns]\n"
          ]
        },
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>ingreso_mensual</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>7521.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>179788.699242</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>59768.917063</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>40000.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>139380.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>179059.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>219747.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>439615.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "       ingreso_mensual\n",
              "count      7521.000000\n",
              "mean     179788.699242\n",
              "std       59768.917063\n",
              "min       40000.000000\n",
              "25%      139380.000000\n",
              "50%      179059.000000\n",
              "75%      219747.000000\n",
              "max      439615.000000"
            ]
          },
          "execution_count": 29,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "print(df_laboral['ingreso_mensual'].dtype)\n",
        "print(df_laboral['ingreso_mensual'].isna().sum())\n",
        "print(df_laboral[['ingreso_mensual']])\n",
        "df_laboral[['ingreso_mensual']].describe()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 30,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JU_CJ8IDawXF",
        "outputId": "f484eb83-3e26-4e06-f8f2-ce417bba89ba"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<StringArray>\n",
            "['tradicional', 'emprendedor',     'PREMIUM', 'Emprendedor',     'Premium',\n",
            " 'Tradicional',           nan,     'premium', 'TRADICIONAL', 'EMPRENDEDOR']\n",
            "Length: 10, dtype: str\n",
            "<StringArray>\n",
            "[ 'traditional',      'premium', 'entrepreneur',  'TRADITIONAL',\n",
            "      'Premium',  'Traditional', 'ENTREPRENEUR',      'PREMIUM',\n",
            " 'Entrepreneur',            nan]\n",
            "Length: 10, dtype: str\n",
            "<StringArray>\n",
            "[                        'Tucumán',                    'buenos aires',\n",
            "                    'Buenos Aires',                         'Córdoba',\n",
            "                        'Santa Fe',                         'Mendoza',\n",
            "                            'CABA', 'Ciudad Autónoma de Buenos Aires',\n",
            "                           'Bs As']\n",
            "Length: 9, dtype: str\n",
            "<StringArray>\n",
            "['divorciado', 'soltero', 'casado', 'viudo']\n",
            "Length: 4, dtype: str\n",
            "<StringArray>\n",
            "['terciario', 'universitario', 'secundario', nan, 'posgrado']\n",
            "Length: 5, dtype: str\n",
            "<StringArray>\n",
            "['empleado', 'desempleado', 'independiente', 'monotributista']\n",
            "Length: 4, dtype: str\n"
          ]
        }
      ],
      "source": [
        "print(df_cl_offline['segmento'].unique())\n",
        "print(df_cl_online['segment'].unique())\n",
        "print(df_demo['provincia'].unique())\n",
        "print(df_demo['estado_civil'].unique())\n",
        "print(df_demo['nivel_educativo'].unique())\n",
        "print(df_laboral['situacion_laboral'].unique())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 31,
      "metadata": {
        "id": "fzNQjZMdbWP9"
      },
      "outputs": [],
      "source": [
        "# Diccionario de mapeo para segmento (unificando a español, minúsculas)\n",
        "mapa_segmento_offline = {\n",
        "    'tradicional': 'tradicional', 'TRADICIONAL': 'tradicional', 'Tradicional': 'tradicional',\n",
        "    'emprendedor': 'emprendedor', 'EMPRENDEDOR': 'emprendedor', 'Emprendedor': 'emprendedor',\n",
        "    'premium': 'premium', 'PREMIUM': 'premium', 'Premium': 'premium',\n",
        "}\n",
        "mapa_segmento_online = {\n",
        "    'traditional': 'tradicional', 'TRADITIONAL': 'tradicional', 'Traditional': 'tradicional',\n",
        "    'entrepreneur': 'emprendedor', 'ENTREPRENEUR': 'emprendedor', 'Entrepreneur': 'emprendedor',\n",
        "    'premium': 'premium', 'PREMIUM': 'premium', 'Premium': 'premium',\n",
        "}\n",
        "\n",
        "df_cl_offline['segmento'] = df_cl_offline['segmento'].map(mapa_segmento_offline)\n",
        "df_cl_online['segment'] = df_cl_online['segment'].map(mapa_segmento_online)\n",
        "\n",
        "# Diccionario de mapeo para provincia\n",
        "mapa_provincia = {\n",
        "    'buenos aires': 'Buenos Aires', 'Buenos Aires': 'Buenos Aires', 'Bs As': 'Buenos Aires',\n",
        "    'CABA': 'CABA', 'Ciudad Autónoma de Buenos Aires': 'CABA',\n",
        "    'Tucumán': 'Tucumán', 'Córdoba': 'Córdoba', 'Santa Fe': 'Santa Fe', 'Mendoza': 'Mendoza',\n",
        "}\n",
        "df_demo['provincia'] = df_demo['provincia'].map(mapa_provincia)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 32,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CkarwRMvbZ5g",
        "outputId": "8cc98490-82f1-43a3-c1aa-49300ad28c7f"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<StringArray>\n",
            "['tradicional', 'emprendedor', 'premium', nan]\n",
            "Length: 4, dtype: str\n",
            "<StringArray>\n",
            "['tradicional', 'premium', 'emprendedor', nan]\n",
            "Length: 4, dtype: str\n",
            "<StringArray>\n",
            "['Tucumán', 'Buenos Aires', 'Córdoba', 'Santa Fe', 'Mendoza', 'CABA']\n",
            "Length: 6, dtype: str\n"
          ]
        }
      ],
      "source": [
        "print(df_cl_offline['segmento'].unique())\n",
        "print(df_cl_online['segment'].unique())\n",
        "print(df_demo['provincia'].unique())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 33,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DTB86WnLgkUq",
        "outputId": "30035a1c-6c9b-438d-fc86-fb6e67e46392"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: sqlalchemy in c:\\users\\notebook\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (2.0.52)\n",
            "Requirement already satisfied: pymysql in c:\\users\\notebook\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (1.2.0)\n",
            "Requirement already satisfied: greenlet>=1 in c:\\users\\notebook\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from sqlalchemy) (3.5.5)\n",
            "Requirement already satisfied: typing-extensions>=4.6.0 in c:\\users\\notebook\\appdata\\roaming\\python\\python313\\site-packages (from sqlalchemy) (4.16.0)\n"
          ]
        },
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "\n",
            "[notice] A new release of pip is available: 25.2 -> 26.2.1\n",
            "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
          ]
        }
      ],
      "source": [
        "!pip install sqlalchemy pymysql"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 34,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 530
        },
        "id": "QZrXbMV1gpRI",
        "outputId": "0059eccf-94dd-4f06-8f9e-1d1144278ed2"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Carga completa\n"
          ]
        }
      ],
      "source": [
        "from sqlalchemy import create_engine\n",
        "\n",
        "engine = create_engine(\"mysql+pymysql://root:33226305@localhost:3306/fintech_challenge\")\n",
        "\n",
        "df_cl_offline.to_sql('stg_clientes_offline', engine, if_exists='replace', index=False)\n",
        "df_cl_online.to_sql('stg_clientes_online', engine, if_exists='replace', index=False)\n",
        "df_prestamos.to_sql('stg_prestamos', engine, if_exists='replace', index=False)\n",
        "df_demo.to_sql('stg_variables_demografica', engine, if_exists='replace', index=False)\n",
        "df_laboral.to_sql('stg_variables_laboral', engine, if_exists='replace', index=False)\n",
        "\n",
        "print(\"Carga completa\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 35,
      "metadata": {},
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Windows\n",
            "DESKTOP-96R71FU\n"
          ]
        }
      ],
      "source": [
        "import platform\n",
        "print(platform.system())\n",
        "print(platform.node())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 36,
      "metadata": {},
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>id_cliente</th>\n",
              "      <th>fecha_alta</th>\n",
              "      <th>sucursal</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>6338</th>\n",
              "      <td>370</td>\n",
              "      <td>2023-12-07</td>\n",
              "      <td>Sucursal Sur</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5001</th>\n",
              "      <td>370</td>\n",
              "      <td>2023-12-07</td>\n",
              "      <td>Sucursal Norte</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>257</th>\n",
              "      <td>430</td>\n",
              "      <td>2021-10-28</td>\n",
              "      <td>Sucursal Sur</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6655</th>\n",
              "      <td>430</td>\n",
              "      <td>2021-10-28</td>\n",
              "      <td>Casa Matriz</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4056</th>\n",
              "      <td>469</td>\n",
              "      <td>2023-09-19</td>\n",
              "      <td>Sucursal Centro</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>875</th>\n",
              "      <td>469</td>\n",
              "      <td>2023-09-19</td>\n",
              "      <td>Sucursal Sur</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4829</th>\n",
              "      <td>584</td>\n",
              "      <td>2021-04-11</td>\n",
              "      <td>Sucursal Centro</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4421</th>\n",
              "      <td>584</td>\n",
              "      <td>2021-04-11</td>\n",
              "      <td>Sucursal Sur</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3070</th>\n",
              "      <td>719</td>\n",
              "      <td>2023-04-26</td>\n",
              "      <td>Sucursal Sur</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6792</th>\n",
              "      <td>719</td>\n",
              "      <td>2023-04-26</td>\n",
              "      <td>Sucursal Norte</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5679</th>\n",
              "      <td>850</td>\n",
              "      <td>2022-07-12</td>\n",
              "      <td>Casa Matriz</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3854</th>\n",
              "      <td>850</td>\n",
              "      <td>2022-07-12</td>\n",
              "      <td>Sucursal Centro</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1091</th>\n",
              "      <td>867</td>\n",
              "      <td>2023-03-03</td>\n",
              "      <td>Casa Matriz</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6701</th>\n",
              "      <td>867</td>\n",
              "      <td>2023-03-03</td>\n",
              "      <td>Sucursal Norte</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4957</th>\n",
              "      <td>1004</td>\n",
              "      <td>2023-11-14</td>\n",
              "      <td>Sucursal Sur</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1753</th>\n",
              "      <td>1004</td>\n",
              "      <td>2023-11-14</td>\n",
              "      <td>Sucursal Norte</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>848</th>\n",
              "      <td>1050</td>\n",
              "      <td>2022-11-26</td>\n",
              "      <td>Sucursal Centro</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7062</th>\n",
              "      <td>1050</td>\n",
              "      <td>2022-11-26</td>\n",
              "      <td>Sucursal Norte</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4617</th>\n",
              "      <td>1078</td>\n",
              "      <td>2022-10-07</td>\n",
              "      <td>Casa Matriz</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4845</th>\n",
              "      <td>1078</td>\n",
              "      <td>2022-10-07</td>\n",
              "      <td>Sucursal Sur</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "      id_cliente fecha_alta         sucursal\n",
              "6338         370 2023-12-07     Sucursal Sur\n",
              "5001         370 2023-12-07   Sucursal Norte\n",
              "257          430 2021-10-28     Sucursal Sur\n",
              "6655         430 2021-10-28      Casa Matriz\n",
              "4056         469 2023-09-19  Sucursal Centro\n",
              "875          469 2023-09-19     Sucursal Sur\n",
              "4829         584 2021-04-11  Sucursal Centro\n",
              "4421         584 2021-04-11     Sucursal Sur\n",
              "3070         719 2023-04-26     Sucursal Sur\n",
              "6792         719 2023-04-26   Sucursal Norte\n",
              "5679         850 2022-07-12      Casa Matriz\n",
              "3854         850 2022-07-12  Sucursal Centro\n",
              "1091         867 2023-03-03      Casa Matriz\n",
              "6701         867 2023-03-03   Sucursal Norte\n",
              "4957        1004 2023-11-14     Sucursal Sur\n",
              "1753        1004 2023-11-14   Sucursal Norte\n",
              "848         1050 2022-11-26  Sucursal Centro\n",
              "7062        1050 2022-11-26   Sucursal Norte\n",
              "4617        1078 2022-10-07      Casa Matriz\n",
              "4845        1078 2022-10-07     Sucursal Sur"
            ]
          },
          "execution_count": 36,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "conflictivos = df_cl_offline[df_cl_offline.duplicated('id_cliente', keep=False)]\n",
        "conflictivos.sort_values('id_cliente')[['id_cliente','fecha_alta','sucursal']].head(20)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 37,
      "metadata": {},
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Segmento distinto: 0\n",
            "Fecha de nacimiento distinta: 0\n",
            "Empty DataFrame\n",
            "Columns: [id_cliente, fecha_nacimiento, customer_id, birth_date]\n",
            "Index: []\n",
            "Nombre distinto (ambos con dato): 0\n"
          ]
        }
      ],
      "source": [
        "common_ids = set(df_cl_offline['id_cliente']) & set(df_cl_online['customer_id'])\n",
        "\n",
        "# 1. Segmento\n",
        "off = df_cl_offline[df_cl_offline['id_cliente'].isin(common_ids)][['id_cliente','segmento']].dropna()\n",
        "on = df_cl_online[df_cl_online['customer_id'].isin(common_ids)][['customer_id','segment']].dropna()\n",
        "merged = off.merge(on, left_on='id_cliente', right_on='customer_id')\n",
        "conflictos_segmento = merged[merged['segmento'] != merged['segment']]\n",
        "print(f\"Segmento distinto: {len(conflictos_segmento)}\")\n",
        "\n",
        "# 2. Fecha de nacimiento (mismo dato biológico, no debería diferir)\n",
        "off_fn = df_cl_offline[df_cl_offline['id_cliente'].isin(common_ids)][['id_cliente','fecha_nacimiento']].dropna()\n",
        "on_fn = df_cl_online[df_cl_online['customer_id'].isin(common_ids)][['customer_id','birth_date']].dropna()\n",
        "merged_fn = off_fn.merge(on_fn, left_on='id_cliente', right_on='customer_id')\n",
        "conflictos_fn = merged_fn[merged_fn['fecha_nacimiento'] != merged_fn['birth_date']]\n",
        "print(f\"Fecha de nacimiento distinta: {len(conflictos_fn)}\")\n",
        "print(conflictos_fn.head(10))\n",
        "\n",
        "# 3. Nombre y apellido (por si acaso, mismo criterio que fecha_nacimiento)\n",
        "off_n = df_cl_offline[df_cl_offline['id_cliente'].isin(common_ids)][['id_cliente','nombre','apellido']]\n",
        "on_n = df_cl_online[df_cl_online['customer_id'].isin(common_ids)][['customer_id','first_name','last_name']]\n",
        "merged_n = off_n.merge(on_n, left_on='id_cliente', right_on='customer_id')\n",
        "conflictos_nombre = merged_n[(merged_n['nombre'] != merged_n['first_name']) & merged_n['nombre'].notna() & merged_n['first_name'].notna()]\n",
        "print(f\"Nombre distinto (ambos con dato): {len(conflictos_nombre)}\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 38,
      "metadata": {},
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "count    3848.0\n",
            "mean        0.0\n",
            "std         0.0\n",
            "min         0.0\n",
            "25%         0.0\n",
            "50%         0.0\n",
            "75%         0.0\n",
            "max         0.0\n",
            "Name: gap_dias, dtype: float64\n",
            "\n",
            "Casos donde online es ANTERIOR a offline (gap negativo): 0\n",
            "Casos donde coinciden exactamente (gap = 0): 3848\n"
          ]
        }
      ],
      "source": [
        "common_ids = set(df_cl_offline['id_cliente']) & set(df_cl_online['customer_id'])\n",
        "\n",
        "off_fa = df_cl_offline[df_cl_offline['id_cliente'].isin(common_ids)][['id_cliente','fecha_alta']]\n",
        "on_fa = df_cl_online[df_cl_online['customer_id'].isin(common_ids)][['customer_id','signup_date']]\n",
        "merged_fa = off_fa.merge(on_fa, left_on='id_cliente', right_on='customer_id')\n",
        "\n",
        "merged_fa['gap_dias'] = (merged_fa['signup_date'] - merged_fa['fecha_alta']).dt.days\n",
        "print(merged_fa['gap_dias'].describe())\n",
        "print()\n",
        "print(\"Casos donde online es ANTERIOR a offline (gap negativo):\", (merged_fa['gap_dias'] < 0).sum())\n",
        "print(\"Casos donde coinciden exactamente (gap = 0):\", (merged_fa['gap_dias'] == 0).sum())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 39,
      "metadata": {},
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "9482\n"
          ]
        }
      ],
      "source": [
        "lab_ids = set(df_laboral['id_cliente'])\n",
        "dem_ids = set(df_demo['id_cliente'])\n",
        "print(len(lab_ids | dem_ids))"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.13.7"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
