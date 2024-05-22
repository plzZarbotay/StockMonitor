<template>
  <div class="not-found">
    <h1>404</h1>
    <p>Упс! Страница, которую вы ищете, не существует.</p>
    <router-link to="/" class="go-back">Вернуться назад</router-link>
  </div>
</template>

<script>
export default {
  name: "NotFound",
};
</script>

<style scoped>
.not-found {
  text-align: center;
  margin-top: 50px;
}
.go-back {
  color: #42b983;
}
</style>
