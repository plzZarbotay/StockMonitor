<template>
  <div
    :class="{
      light_body: isLightTheme,
      dark_body: !isLightTheme,
    }"
  >
    <TopBarView />
    <div class="name_box">
      <img class="avatar" src="./static/user-icon.png" />
      <div class="namevalue" id="name">
        {{ user ? user.email.split("@")[0] : "Name Glitch" }}
      </div>
    </div>
    <button class="logout_button" @click="redirectToLogoutPage">Выход</button>
    <div class="buttons_wrapper">
      <div class="income_per_day_box">
        <div class="income_per_day_header">Баланс</div>
        <div class="income_per_day_value">{{ balance }}</div>
      </div>
      <div class="total_value_box">
        <div class="total_value_header">Стоимость</div>
        <div class="income_per_day_value">183,256₽</div>
      </div>
      <div class="profitability_box">
        <div class="profitability_box_header">Общий доход</div>
        <div class="profitability_box_value">+63%</div>
      </div>
    </div>

    <div class="data_container">
      <div class="data_container_header">
        <span>Название</span> <span>Количество</span>
        <span>Цена за единицу</span> <span>Общая цена</span> <span>Доля</span>
      </div>
      <div v-if="stocks.length === 0" class="no_data_message">
        Транзакции не были совершены
      </div>
      <div
        v-else
        class="stock_item"
        v-for="stock in stocks"
        :key="stock.stock.ticker"
      >
        <span>{{ stock.stock.name }}</span>
        <span>{{ stock.volume }}</span>
        <span>{{ stock.stock.last_price }}</span>
        <!-- Add other properties as needed -->
      </div>
    </div>
  </div>
</template>

<script>
import TopBarView from "@/components/TopBarView.vue";
import { mapState } from "vuex";
import { mapActions, mapGetters } from "vuex";
export default {
  computed: {
    ...mapState("auth", ["user"]),
    ...mapGetters("auth", ["balance"]),
    ...mapGetters(["isLightTheme"]),
  },
  methods: {
    async loadBalance() {
      await this.getBalance();
      await this.loadOwnedStocks();
    },
    ...mapActions("auth", ["getBalance"]),
    redirectToLogoutPage() {
      this.$router.push("/auth/logout");
    },
    async loadOwnedStocks() {
      try {
        await this.getOwnedStocks();
      } catch (error) {
        console.error("Error fetching owned stocks:", error);
      }
    },
  },
  components: {
    TopBarView,
  },
  mounted() {
    this.loadBalance();
  },
  data() {
    return {
      stocks: [],
    };
  },
};
</script>

<style>
.logout_button {
  position: absolute;
  width: 180px;
  height: 54.01px;
  right: 1.1%;
  top: 100px;
  display: flex;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
  border: 5px solid transparent;
  border-radius: 40px;
  background: rgb(70, 62, 127);
  color: white;
  padding: 10px;
  font-size: 20px;
}

.light_body {
  background-color: #e0e0e0;
  height: 1000px;
  transition: transform 0.4s ease;
}

.logout_button:hover {
  cursor: pointer;
  background-color: rgb(156, 198, 235);
  color: black;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

body {
  background-color: rgba(10, 20, 41, 1);
  color: white;
  font-family: system-ui;
  font-size: 26px;
  font-weight: 600;
}

span {
  font-size: 20px;
  font-weight: 400;
  margin: 0px;
}

.top_header_wrapper {
  display: flex;
  justify-content: center;
}

.top_header {
  display: flex;
  position: absolute;
  width: 567px;
  height: 75px;
  justify-content: center;
  align-items: center;
  top: 0px;

  color: white;
  text-decoration-line: underline;
  text-underline-offset: 8px;
  text-decoration-thickness: 3px;

  background: #335062;
  box-shadow: 0px 0px 9.8px 4px rgba(0, 0, 0, 0.25);
  border-radius: 0px 0px 29px 29px;
}

.name_box {
  display: flex;
  align-items: center;
  width: 421px;
  height: 118px;
  margin-left: -1%;
  margin-top: 6%;
  color: #42b983;
  background: #335062;
  box-shadow: 0px 0px 9.8px 4px rgba(0, 0, 0, 0.25);
  border-radius: 0px 29px 29px 0px;
}

.namevalue {
  color: #42b983;
  margin: 20px;
}

.avatar {
  color: #42b983;
  margin: 50px;
  width: 90px;
}

.buttons_wrapper {
  color: #42b983;
  display: flex;
  justify-content: space-between;
  margin: 0 auto;
  margin-top: 4%;
  width: 1309px;
  height: 118px;
}

.income_per_day_box {
  display: flex;
  color: #42b983;
  align-items: center;
  justify-content: center;
  width: 400px;
  height: 118px;
  left: 0;

  background: #335062;
  box-shadow: 0px 0px 9.8px 4px rgba(0, 0, 0, 0.25);
  border-radius: 29px;
}

.total_value_box {
  display: flex;
  width: 407px;
  height: 118px;
  justify-content: center;
  background: #335062;
  box-shadow: 0px 0px 9.8px 4px rgba(0, 0, 0, 0.25);
  border-radius: 29px;
}

.profitability_box {
  display: flex;
  width: 407px;
  height: 118px;
  background: #335062;
  box-shadow: 0px 0px 9.8px 4px rgba(0, 0, 0, 0.25);
  border-radius: 29px;
}

.income_per_day_header,
.total_value_header,
.profitability_box_header {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 200px;
  height: 118px;
  color: rgba(255, 255, 255, 0.5);
}

.income_per_day_value,
.total_value_value,
.profitability_box_value {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 200px;
  height: 118px;
}

.data_container {
  color: #42b983;
  display: flex;
  margin: 0 auto;
  margin-top: 2%;
  width: 1309px;
  height: 456px;

  background: #335062;
  border-radius: 29px;
}

.data_container_header {
  width: 1309px;
  height: 80px;
  left: 65px;
  top: 512px;
  display: flex;
  justify-content: space-between;
  align-items: center;

  background: rgba(0, 0, 0, 0.49);
  border-radius: 29px 29px 0px 0px;
}
</style>
