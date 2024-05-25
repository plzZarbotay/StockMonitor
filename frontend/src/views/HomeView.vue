<template>
  <div :class="{ light_body1: isLightTheme, dark_body: !isLightTheme }">
    <TopBarView />
    <h1>
      <span class="title__text">Stock Market Monitor</span>
    </h1>
    <div>
      <span class="left_line"><img src=".\static\Left_line.png" /></span>
      <span class="right_line"><img src=".\static\Rignt_line.png" /></span>
      <span class="text_und_tit_text"
        ><b>Инструмент</b> для <b>анализа данных рынка</b>, предоставляющий
        возможность парсинга данных о объеме продаж, трендах покупателей и
        динамике из дня в день.</span
      >
      <span class="dedook"
        ><img src=".\static\dedook.svg" width="auto" height="auto"
      /></span>
      <span class="top_arrows">
        <img src=".\static\top_arrows.png" width="1130px" height="30px" />
      </span>
      <button
        :class="{
          podrobnee_light: isLightTheme,
          podrobnee_dark: !isLightTheme,
        }"
        @click="redirectToAboutPage"
      >
        Подробнее
      </button>
      <span class="bottom_arrows"
        ><img src=".\static\bottom_arrows.png" width="1130px" height="30px"
      /></span>
      <div class="rectangles_wrapper1">
        <div class="rectangles1">
          <span class="teacker">BTC</span>
          <span class="teacker" style="color: #2df50c">+0,25%</span>
        </div>
        <div class="rectangles2">
          <span class="teacker">ETH</span>
          <span class="teacker" style="color: #2df50c">+0,5%</span>
        </div>
        <div class="rectangles3">
          <span class="teacker">TON</span>
          <span class="teacker" style="color: #da1111">-11,5%</span>
        </div>
        <div class="rectangles4">
          <span class="teacker">DOGE</span>
          <span class="teacker" style="color: #2df50c">+0,65%</span>
        </div>
        <div class="rectangles5">
          <span class="teacker">BNB</span>
          <span class="teacker" style="color: #da1111">-0,11%</span>
        </div>
      </div>
      <span class="analitycs_market">Аналитика рынка</span>

      <span class="SMM_text"
        >Stock Market Monitor - инструмент для анализа данных рынка,
        предоставляющий возможность парсинга данных о объеме продаж, трендах
        покупателей и динамике.</span
      >
      <span class="graphics"
        ><img src=".\static\grafhics.svg" width="450px" height="470px"
      /></span>
      <div class="icon_wrapper">
        <span class="left_icon"
          ><img src=".\static\left_icon.svg" width="50px" height="52px"
        /></span>
        <span class="sr_icon"
          ><img src=".\static\sr_icon.svg" width="50px" height="53px"
        /></span>
        <span class="right_icon"
          ><img src=".\static\right_icon.svg" width="50px" height="53px"
        /></span>
        <span class="right_rec"
          ><img src=".\static\right_rec.svg" width="135px" height="53px"
        /></span>
      </div>
      <span class="car"><img src=".\static\car.svg" /></span>
      <span class="top_arrows2"
        ><img src=".\static\top_arrows.png" width="1130px" height="30px"
      /></span>
      <span class="bottom_arrows2"
        ><img src=".\static\bottom_arrows.png" width="1130px" height="30px"
      /></span>
      <span class="blog">Наши Преимущества</span>
      <span class="text_blog"
        >Наш продукт предоставляет возможность поиска информации более чем по
        200 компаниям, а также включает базу данных с более чем 17 миллионами
        записей.</span
      >
      <div class="rectangles_wrapper2">
        <div class="rectangles6">
          <span class="teacker">BTC</span>
          <span class="teacker" style="color: #2df50c">+0,25%</span>
        </div>
        <div class="rectangles7">
          <span class="teacker">ETH</span>
          <span class="teacker" style="color: #2df50c">+0,5%</span>
        </div>
        <div class="rectangles8">
          <span class="teacker">TON</span>
          <span class="teacker" style="color: #da1111">-11,5%</span>
        </div>
        <div class="rectangles9">
          <span class="teacker">DOGE</span>
          <span class="teacker" style="color: #2df50c">+0,65%</span>
        </div>
        <div class="rectangles10">
          <span class="teacker">BNB</span>
          <span class="teacker" style="color: #da1111">-0,11%</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.light_body1 {
  height: 2900px;
  background-color: #e0e0e0;
}

.title__text {
  display: flex;
  font-size: 60px;
  font-family: system-ui;
  background: linear-gradient(
    90deg,
    rgba(48, 44, 208, 1) 0%,
    rgba(119, 54, 54, 1) 180%
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  position: absolute;
  width: 1440px;
  left: 8%;
  top: 220px;
}

/* Войти */
.to_come_in {
  display: flex;
  position: absolute;
  width: 184px;
  height: 47.01px;
  left: 87%;
  top: 25px;
  font-size: 18px;
  font-family: system-ui;
}
/* top_grad_sq */
.top_grad_sq {
  position: absolute;
  width: 184px;
  height: 46px;
  left: 1033px;
  top: 15px;
}

/* Рынок */
.market {
  display: flex;
  position: absolute;
  width: 184px;
  height: 47.01px;
  left: 130px;
  top: 25px;
  font-family: "system-ui";
  background: linear-gradient(90deg, #7000ff 0%, #872626 180%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}
/* logo1 */
.logo1 {
  position: absolute;
  width: 5px;
  height: 9px;
  left: 40px;
  top: 17px;
}

/* search_icon */
.search_icon {
  position: absolute;
  width: 5px;
  height: 9px;
  left: 390px;
  top: 28px;
}

/* Left_line */
.left_line {
  position: absolute;
  width: 56px;
  height: 2833px;
  left: 0.5%;
  top: 1.2%;
}

/* Right_line */
.right_line {
  position: absolute;
  width: 60px;
  height: 2829px;
  right: 0.6%;
  top: 1.2%;
}

/* Аналитика */
.analytics {
  display: flex;
  position: absolute;
  width: 184px;
  height: 47.01px;
  left: 230px;
  top: 25px;
  font-family: "system-ui";
  background: linear-gradient(90deg, #7000ff 0%, #872626 180%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.top_rectangle {
  display: flex;
  position: absolute;
  width: 1250px;
  height: 70px;
  left: 0px;
  top: 1px;

  background: #0a1429;
  box-shadow: 0px 3px 9px rgba(0, 0, 0, 0.25);
}

.search_text::placeholder {
  font-size: 12px;
  font-family: system-ui;
  color: rgba(84, 129, 143, 1);
}

/* dedook */
.dedook {
  position: absolute;
  width: 316px;
  height: 580px;
  left: 65%;
  top: 161px;
  transition: transform 1s ease;
}

.dedook:hover {
  transform: translateY(-20px);
}

/* text under title_text*/
.text_und_tit_text {
  position: absolute;
  text-align: left;
  width: 553px;
  height: 159px;
  left: 8%;
  top: 340px;
  font-family: "system-ui";
  font-style: normal;
  font-weight: 200;
  font-size: 26px;
  line-height: 31px;

  color: #54818f;
}

/* Podrobnee */
.podrobnee_dark {
  position: absolute;
  width: 273px;
  height: 54.01px;
  left: 7.8%;
  top: 520px;
  display: flex;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
  border: 5px solid transparent;
  border-radius: 40px;
  background: rgb(62, 46, 178);
  color: white;
  padding: 10px;
  font-size: 20px;
}

.podrobnee_light {
  position: absolute;
  width: 273px;
  height: 54.01px;
  left: 7.8%;
  top: 520px;
  display: flex;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
  border: 5px solid transparent;
  border-radius: 40px;
  background-color: #548f64;
  color: white;
  padding: 10px;
  font-size: 20px;
}

.podrobnee_dark:hover {
  cursor: pointer;
  transition: transform 0.3s ease;
  transform: scale(1.05);
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  background: rgb(75, 59, 196);
}

/* top_arrows */
.top_arrows {
  position: absolute;
  left: 0;
  right: 0;
  margin: auto;
  top: 906px;
  opacity: 0.45;
}

/* Rectangles */
.rectangles1,
.rectangles2,
.rectangles3,
.rectangles4,
.rectangles5,
.rectangles6,
.rectangles7,
.rectangles8,
.rectangles9,
.rectangles10 {
  top: 0px;
  margin: 0 auto;
  cursor: none;
}

.rectangles_wrapper1,
.rectangles_wrapper2 {
  position: absolute;
  display: flex;
  top: 970px;
  width: 1200px;
  left: 0;
  right: 0;
  margin: auto;
  justify-content: space-between;
}

.rectangles_wrapper2 {
  top: 2370px;
}

.rectangles1 {
  width: 181.18px;
  height: 57.72px;
  display: flex;
  background: #232d5371;
  box-shadow: 0px 3px 9px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
}

.rectangles1:hover,
.rectangles2:hover,
.rectangles3:hover,
.rectangles4:hover,
.rectangles5:hover,
.rectangles6:hover,
.rectangles7:hover,
.rectangles8:hover,
.rectangles9:hover,
.rectangles10:hover {
  background: #34407171;
  transform: scale(1.02);
  cursor: auto;
}

.rectangles2 {
  width: 181.18px;
  height: 57.72px;
  display: flex;
  background: #232d5371;
  box-shadow: 0px 3px 9px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
}

.rectangles3 {
  width: 181.18px;
  height: 57.72px;
  display: flex;
  background: #232d5371;
  box-shadow: 0px 3px 9px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
}

.rectangles4 {
  width: 181.18px;
  height: 57.72px;
  display: flex;
  background: #232d5371;
  box-shadow: 0px 3px 9px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
}

.rectangles5 {
  width: 181.18px;
  height: 57.72px;
  display: flex;
  background: #232d5371;
  box-shadow: 0px 3px 9px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
}

.teacker {
  display: flex;
  width: 95px;
  font-family: "system-ui";
  font-style: normal;
  align-items: center;
  text-align: center;
  justify-content: center;
  color: #ffffff;
}

.bottom_arrows {
  position: absolute;
  left: 0;
  right: 0;
  margin: 0;
  top: 1056px;

  opacity: 0.45;
}

/*Аналитика рынка */
.analitycs_market {
  position: absolute;
  width: 582px;
  height: 76px;
  left: 105px;
  top: 1290px;
  font-family: "system-ui";
  font-style: normal;
  font-weight: 500;
  font-size: 51px;
  line-height: 31px;
  background: linear-gradient(90deg, #7000ff 0%, #872626 180%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

/* Stock Market Monitor */

.SMM_text {
  position: absolute;
  width: 553px;
  height: 217px;
  left: 105px;
  top: 1370px;

  font-family: "system-ui";
  font-style: normal;
  font-weight: 200;
  font-size: 26px;
  line-height: 31px;
  display: flex;
  align-items: center;
  justify-content: space-between;

  color: #54818f;
}

/* Graphics */
.graphics {
  position: absolute;
  width: 520px;
  height: 432.64px;
  left: 870px;
  top: 1220px;
}

.icon_wrapper {
  display: flex;
  position: absolute;
  right: 20%;
  width: 400px;
  top: 1660px;
  justify-content: space-between;
}

/* left_icon unger graf*/
.left_icon {
  margin: 0px;
}

.left_icon:hover {
  transform: scale(1.1);
}

/* sr_icon under graf */
.sr_icon {
  margin: 0px;
}

.sr_icon:hover {
  transform: scale(1.1);
}

/* right_icon under graf */
.right_icon {
  margin: 0px;
}

.right_icon:hover {
  transform: scale(1.1);
}

/* right_rec under graf */
.right_rec {
  margin: 0px;
}

.right_rec:hover {
  transform: scale(1.1);
}

/* Машина 1 */
.car {
  position: absolute;
  left: 107px;
  top: 1950px;
}

/* top_arrows2 */
.top_arrows2 {
  position: absolute;
  left: 0;
  right: 0;
  margin: 0;
  top: 2310px;

  opacity: 0.45;
}

/*Блоги */
.blog {
  display: flex;
  position: absolute;
  width: 582px;
  height: 76px;
  left: 150px;
  top: 2090px;
  font-family: "system-ui";
  font-style: normal;
  font-weight: 500;
  font-size: 49px;
  line-height: 31px;
  color: #54818f;
}

.text_blog {
  display: flex;
  position: absolute;
  width: 582px;
  height: 76px;
  left: 150px;
  top: 2170px;
  font-family: "system-ui";
  font-style: normal;
  font-weight: 300;
  font-size: 27px;
  line-height: 31px;
  color: #99beca;
  text-align: left;
}

/* Bottom_rectangles */
.rectangles6 {
  width: 181.18px;
  height: 57.72px;
  display: flex;
  background: #232d5371;
  box-shadow: 0px 3px 9px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
}

.rectangles7 {
  width: 181.18px;
  height: 57.72px;
  display: flex;
  background: #232d5371;
  box-shadow: 0px 3px 9px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
}

.rectangles8 {
  width: 181.18px;
  height: 57.72px;
  display: flex;
  background: #232d5371;
  box-shadow: 0px 3px 9px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
}

.rectangles9 {
  width: 181.18px;
  height: 57.72px;
  display: flex;
  background: #232d5371;
  box-shadow: 0px 3px 9px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
}

.rectangles10 {
  width: 181.18px;
  height: 57.72px;
  display: flex;
  background: #232d5371;
  box-shadow: 0px 3px 9px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
}

/* bottom_arrows2 */
.bottom_arrows2 {
  position: absolute;
  left: 0;
  right: 0;
  margin: 0;
  top: 2456px;

  opacity: 0.45;
}

/* Полоса прокрутки */
::-webkit-scrollbar {
  width: 8px; /* ширина вертикальной полосы прокрутки */
  height: 8px; /* высота горизонтальной полосы прокрутки */
}

/* Ползунок полосы прокрутки */
::-webkit-scrollbar-thumb {
  background-color: #42b983; /* цвет ползунка */
  border-radius: 4px; /* закругленные углы ползунка */
}

/* Ползунок полосы прокрутки при наведении */
::-webkit-scrollbar-thumb:hover {
  background-color: #65e96e; /* цвет ползунка при наведении */
}

/* Фон полосы прокрутки */
::-webkit-scrollbar-track {
  background: #0a1429; /* цвет фона полосы прокрутки */
  border-radius: 4px; /* закругленные углы фона */
}

/* Фон полосы прокрутки при наведении */
::-webkit-scrollbar-track:hover {
  background: #e1e1e1; /* цвет фона полосы прокрутки при наведении */
}
</style>
<script>
import TopBarView from "@/components/TopBarView.vue";
import { mapGetters, mapActions } from "vuex";

export default {
  computed: {
    ...mapGetters(["isLightTheme"]),
  },
  methods: {
    ...mapActions(["toggleTheme"]),
    redirectToAboutPage() {
      this.$router.push("/about");
    },
    toggleTheme() {
      this.$store.dispatch("toggleTheme");
    },
  },
  components: {
    TopBarView,
  },
};
</script>
