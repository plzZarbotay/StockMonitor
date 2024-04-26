<template>
  <div class="top-wrapper">
    <div class="top_left_box">
      <div class="top_box">
        <div class="top_box_header1">{{ name }}</div>
        <img
          src="/static/bx-star.png"
          style="margin-left: -15px; margin-bottom: 3px"
        />
        <img src="/static/bxl-bitcoin.png" style="margin: 10px; height: 70%" />
      </div>
      <img class="chart_box" src="/static/chart.png" />
    </div>

    <div class="right_box">
      <div class="price_container">
        <span class="price_header">Цена</span>
        <span class="price_value" id="price_value">{{ price }}</span>
      </div>
      <div class="buttons_container">
        <button class="buy_button" @click="buyStock">Купить</button>
        <button class="sell_button" @click="sellStock">Продать</button>
      </div>
    </div>
  </div>

  <div class="bottom_container">
    <div class="bottom_box">{{ description }}</div>
  </div>
</template>

<script>
export default {
  props: ["name", "price", "description"],
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
  margin-left: 30px;
}

.top_box_header2 {
  display: flex;
  color: #c9c9c9;
}

.right_box {
  width: 226px;
  height: 259px;
  left: 1389px;
  top: 40px;

  background: #335062;
  border-radius: 29px;
}

.price_container {
  display: flex;
  flex-flow: column wrap;
  margin-left: 20px;
  margin-top: 30px;
}

.price_header {
  color: rgba(255, 255, 255, 0.5);
  margin-bottom: 5px;
}

.price_value {
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

  border-style: hidden;
  background: #309924;
  border-radius: 10px;
}

.sell_button {
  position: absolute;
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
  margin-top: 220px;
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
