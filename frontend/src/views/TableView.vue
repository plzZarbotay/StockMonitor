<template>
  <div
    :class="{
      table_light: isLightTheme,
      table_dark: !isLightTheme,
    }"
  >
    <TopBarView />
    <div class="container">
      <table>
        <thead>
          <tr>
            <th>Название</th>
            <th>Цена</th>
            <th>За 24ч</th>
            <th>Объем торгов за 24ч.</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="row in tableData"
            :key="row.name"
            @click="navigateToStock(row.ticker)"
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
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import TopBarView from "@/components/TopBarView.vue";
import router from "@/router";

export default {
  components: {
    TopBarView,
  },
  computed: {
    ...mapGetters(["isLightTheme"]),
    ...mapGetters(["tableData"]),
  },
  mounted() {
    this.fetchStocks();
  },
  methods: {
    ...mapActions(["fetchStocks"]),
    navigateToStock(ticker) {
      router.push({ name: "stock", params: { ticker } });
    },
  },
};
</script>

<style>
.table_light {
  background-color: #e0e0e0;
  height: 1000px;
}

body {
  font-family: system-ui;
  color: #42b983;
  text-decoration: none;
}

.container {
  display: flex;
  justify-content: center;
  text-align: center;
  margin-top: 20px; /* Чтобы таблица не пересекалась с top bar */
}

thead,
tfoot {
  font-size: large;
  color: #42b983;
  border-bottom: 1px solid #fff;
}

table {
  width: 90%;
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

td {
  color: #fff;
  padding: 8px 10px;
  text-align: center;
}

tr {
  padding: 0;
  margin: 0;
}
</style>
