<template>
  <div>
    <TopBarView />
    <div class="about">
      <h1>Тут будет описание...</h1>
    </div>
  </div>
</template>

<script>
import TopBarView from "@/components/TopBarView.vue";

export default {
  components: {
    TopBarView,
  },
};
</script>

<style scoped>
.about {
  text-align: center;
  margin-top: 80px; /* Отступ сверху, чтобы контент не пересекался с топ-баром */
  color: #42b983;
  font-family: system-ui;
}
</style>
