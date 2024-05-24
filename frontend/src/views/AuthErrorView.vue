<template>
  <div class="auth-error">
    <h1>Доступ запрещен</h1>
    <p>Вы уже вошли в систему и не можете получить доступ к этой странице.</p>
    <div class="go-back" @click="goBack">&#8592; Вернуться</div>
  </div>
</template>

<script>
export default {
  name: "AuthError",
  methods: {
    goBack() {
      this.$router.push("/");
    },
  },
};
</script>

<style scoped>
.auth-error {
  text-align: center;
  padding: 20px;
}

.go-back {
  margin-top: 20px;
  font-size: 24px;
  cursor: pointer;
  color: #42b983;
}

.go-back:hover {
  text-decoration: underline;
}
</style>
