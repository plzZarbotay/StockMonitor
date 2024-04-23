<template>
  <div class="top_box">
    <div class="top_box_header1">Bitcoin</div>
    <div class="top_box_header2">BTC</div>
    <img
      src="/static/bx-star.png"
      style="margin-left: 12px; margin-bottom: 3px"
    />
    <img src="/static/bxl-bitcoin.png" style="margin-left: 400px" />
  </div>
  <div class="right_box">
    <div class="price_container">
      <span class="price_header">Цена</span>
      <span class="price_value" id="price_value">$60,000</span>
    </div>
    <div class="buttons_container">
      <button class="buy_button">Купить</button>
      <button class="sell_button">Продать</button>
    </div>
  </div>
  <div class="bottom_container">
    <div class="bottom_box"></div>
  </div>
</template>

<style>
body {
  background-color: rgba(10, 20, 41, 1);
  color: white;
  font-family: system-ui;
  font-size: 20px;
}

.top_box {
  position: absolute;
  display: flex;
  align-items: center;
  width: 747px;
  height: 104px;
  left: 310px;
  top: 40px;

  background: #335062;
  border-radius: 29px;
}

.top_box_header1 {
  display: flex;
  margin-left: 50px;
}

.top_box_header2 {
  display: flex;
  margin-left: 20px;
  color: #c9c9c9;
}

.right_box {
  position: absolute;
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

.bottom_container {
  display: flex;
  text-align: center;
  justify-content: center;
  margin-top: 640px;
}

.bottom_box {
  display: flex;
  width: 1309px;
  height: 237px;

  background: #335062;
  border-radius: 29px;
}
</style>
