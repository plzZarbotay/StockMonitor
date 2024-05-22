<template>
  <div class="home">
    <TopBarView />
    <h1>Тут будет главная...</h1>
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
.home {
  color: #42b983;
  text-align: center;
}
</style>
