<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import Main from "views/main/Main.vue";
import login from "components/Login.vue";

export default {
  name: "App",
  components: {
    Main,
    login,
  },
  mounted(){
    const user=localStorage.getItem('user')
    this.$store.commit('login',user)
  }
};
</script>

<style>
@import "assets/css/base.css";
</style>
