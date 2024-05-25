<template>
  <div
    :class="{
      desk_light: isLightTheme,
      desk_dark: !isLightTheme,
    }"
  >
    <TopBarView />
    <div class="top-wrapper">
      <div class="top_left_box">
        <div class="top_box">
          <div class="top_box_header1" style="color: #42b983">
            {{ name }} || {ticker}
          </div>
        </div>
        <ChartView class="chart_position" />
      </div>

      <div class="right_box">
        <div class="price_container">
          <span class="price_header">Цена</span>
          <span class="price_value" id="price_value">{{ 1 }}</span>
        </div>
        <div class="buttons_container">
          <button class="buy_button" @click="buyStock">Купить</button>
          <button class="sell_button" @click="sellStock">Продать</button>
        </div>
      </div>
    </div>

    <div class="bottom_container">
      <div class="bottom_box">{{ 1 }}</div>
    </div>
  </div>
</template>

<script>
//import axios from "axios";
import { mapGetters } from "vuex";
import ChartView from "@/components/ChartView.vue";
import TopBarView from "@/components/TopBarView.vue";

export default {
  computed: {
    ...mapGetters(["isLightTheme"]),
  },
  components: {
    ChartView,
    TopBarView,
  },
  props: ["name"],
  methods: {
    buyStock() {
      // Здесь должна быть ваша логика покупки акций
      console.log("Купить акции");
    },
    sellStock() {
      // Здесь должна быть ваша логика продажи акций
      console.log("Продать акции");
    },
  },
};
</script>

<style>
.desk_light {
  background-color: #e0e0e0;
  height: 1000px;
}

body {
  background-color: rgba(10, 20, 41, 1);
  color: white;
  font-family: system-ui;
  font-size: 20px;
}

.top-wrapper {
  justify-content: space-between;
  display: flex;
  margin: auto;
  margin-top: 50px;
  width: 1309px;
  height: 300px;
}

.chart_position {
  top: 20%;
}

.top_left_box {
  display: flex;
  flex-direction: column;
}

.top_box {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 320px;
  height: 104px;
  left: 310px;
  top: 40px;

  background: #335062;
  border-radius: 29px;
}

.top_box_header1 {
  display: flex;
  margin-left: 60px;
}

.top_box_header2 {
  display: flex;
  color: #c9c9c9;
}

.right_box {
  display: flex;
  width: 250px;
  height: 250px;
  left: 10%;
  top: 40px;

  background: #335062;
  border-radius: 29px;
}

.price_container {
  display: flex;
  flex-flow: column wrap;
  margin-left: 20px;
  margin-top: 0px;
}

.price_header {
  position: relative;
  color: rgba(255, 255, 255, 0.5);
  margin-bottom: 5px;
  left: 160%;
  top: 6%;
  color: white;
  font-size: 20px;
}

.price_value {
  position: relative;
  top: 10%;
  left: 160%;
  color: white;
  font-weight: bolder;
  font-size: 25px;
}

.buttons_container {
  display: flex;
  text-align: center;
  justify-content: center;
  height: 50px;
  margin: 20px;
}

.buy_button {
  position: absolute;
  width: 184px;
  height: 46.14px;
  color: white;
  font-family: system-ui;
  font-size: 18px;
  font-weight: 600;
  top: 30%;
  left: 75.7%;
  border-style: hidden;
  background: #309924;
  border-radius: 10px;
}

.sell_button {
  position: absolute;
  top: 30%;
  left: 75.7%;
  width: 184px;
  height: 46.14px;
  margin-top: 70px;
  color: white;
  font-family: system-ui;
  font-size: 18px;
  font-weight: 600;

  border-style: hidden;
  background: #e23f3f;
  border-radius: 10px;
}

.chart_box {
  display: flex;
  margin-top: 30px;
}

.bottom_container {
  display: flex;
  text-align: center;
  justify-content: center;
  margin-top: 20%;
}

.bottom_box {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 1309px;
  height: 50px;

  background: #335062;
  border-radius: 29px;
}
</style>
