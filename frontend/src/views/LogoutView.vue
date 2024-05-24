<template>
  <div class="logout-container">
    <h2>Производится выход...</h2>
  </div>
</template>

<script>
export default {
  created() {
    this.logoutUser();
  },
  methods: {
    async logoutUser() {
      await this.$store.dispatch("auth/logout");
      this.$store.dispatch("auth/redirectAfterLogout");
    },
  },
};
</script>

<style>
.logout-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  font-size: 24px;
}
</style>
