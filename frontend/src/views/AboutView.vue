<template>
  <div :class="{ light: isLightTheme, dark: !isLightTheme }">
    <TopBarView />
    <span class="rec_about_us"><img src=".\static\About us.svg" /></span>
    <span class="top_rec"
      ><img src=".\static\top_rec.svg" weigh="80%" height="80%"
    /></span>
    <span class="sr_rec"><img src=".\static\sr_rec.svg" /></span>
    <span class="bot_rec"><img src=".\static\bot_rec.svg" /></span>
    <span class="text_und_tit_text"
      ><b>SMM</b> - это веб-интерфейс, где парсятся данные, строятся красивые
      отчеты и производится анализ фондового рынка в целом: объем продаж, тренды
      покупателей, динамика изо дня в день.</span
    >
    <span class="join"><img src=".\static\join.svg" /></span>
  </div>
</template>

<style scoped>
.light {
  background-color: #e0e0e0;
  height: 800px;
}

body {
  font-family: system-ui;
  height: 1000px;
}

.top_grad_sq {
  position: absolute;
  width: 184px;
  height: 46px;
  left: 1033px;
  top: 15px;
}

.to_come_in {
  display: flex;
  position: absolute;
  width: 184px;
  height: 47.01px;
  left: 1100px;
  top: 25px;
  font-size: 18px;
  font-family: system-ui;
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

.search_text::placeholder {
  font-size: 12px;
  font-family: system-ui;
  color: rgba(84, 129, 143, 1);
}

/* search_icon */
.search_icon {
  position: absolute;
  width: 5px;
  height: 9px;
  left: 390px;
  top: 28px;
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

.rec_about_us {
  position: absolute;
  width: 15%;
  left: -1%;
  top: 20%;
}

.top_rec {
  position: absolute;
  width: 509px;
  height: 208px;
  left: 913px;
  top: 100px;
}

.sr_rec {
  position: absolute;
  width: 509px;
  height: 208px;
  left: 817px;
  top: 260px;
}

.bot_rec {
  position: absolute;
  width: 509px;
  height: 208px;
  left: 663px;
  top: 470px;
}

/* text under title_text*/
.text_und_tit_text {
  position: absolute;
  width: 445px;
  left: 37px;
  top: 340px;
  font-family: "system-ui";
  font-weight: 500;
  font-size: 26px;
  line-height: 31px;

  color: #54818f;
}

.join {
  position: absolute;
  width: 338px;
  height: 88px;
  left: 20px;
  top: 580px;
}
</style>

<script>
import { mapGetters, mapActions } from "vuex";
import TopBarView from "@/components/TopBarView.vue";

export default {
  computed: {
    ...mapGetters(["isLightTheme"]),
  },
  methods: {
    ...mapActions(["toggleTheme"]),
    toggleTheme() {
      this.$store.dispatch("toggleTheme");
    },
  },
  components: {
    TopBarView,
  },
};
</script>
