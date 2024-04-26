<template>
  <div class="container">
    <table>
      <thead>
        <tr>
          <th>Название</th>
          <th>Цена/ед</th>
          <th>Изменение</th>
          <th>Объем торгов</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(row, value) in tableData"
          :key="value"
          @click="
            $router.push({
              name: 'stock',
              params: {
                name: row.name,
                price: row.price,
                description: row.description,
              },
            })
          "
        >
          <td>
            <span>{{ row.name }}</span>
          </td>
          <td>{{ row.price }}</td>
          <td
            :style="{
              color: row.change.startsWith('+')
                ? 'Lime'
                : row.change.startsWith('-')
                ? 'OrangeRed'
                : 'white',
            }"
          >
            {{ row.change }}
          </td>
          <td>{{ row.volume }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tableData: [
        {
          name: "Tesla, Inc.",
          price: "20$",
          change: "+10%",
          volume: "$122k",
          description: "Описание акции Tesla",
        },
        {
          name: "Yandex, Inc.",
          price: "0.01$",
          change: "-90%",
          volume: "$1k",
          description: "Описание акции Yandex",
        },
        {
          name: "Google, Inc.",
          price: "15$",
          change: "-11%",
          volume: "$1222k",
          description: "Описание акции Google",
        },
        {
          name: "Google, Inc.",
          price: "15$",
          change: "+11%",
          volume: "$1222k",
          description: "Описание акции Google",
        },
      ],
    };
  },
};
</script>

<style>
body {
  font-family: system-ui;
  color: white;
}

.container {
  display: flex;
  justify-content: center;
  text-align: center;
}

thead,
tfoot {
  font-size: large;
  color: #fff;
  border-bottom: 1px solid #fff;
}

table {
  position: absolute;
  width: 90%;
  height: auto;
  top: 82px;
  background: #335062;
  border-radius: 29px;
  border-collapse: collapse;
  font-family: sans-serif;
  font-size: 0.8rem;
  letter-spacing: 1px;
}
tbody {
  font-size: medium;
}

th,
td {
  color: #fff;
  padding: 8px 10px;
}
tr {
  padding: 0;
  margin: 0;
}
td {
  text-align: center;
}
</style>
