<template>
  <div>
    <div class="login">
      <el-input v-model="email" placeholder="请输入邮箱"></el-input>
      <el-input v-model="password" placeholder="请输入密码"></el-input>
      <el-button type="primary" plain @click="login">登录</el-button>
    </div>
    <div class="register">
      <el-input v-model="email" placeholder="请输入邮箱"></el-input>
      <el-input v-model="username" placeholder="请输入用户名"></el-input>
      <el-input
        v-model="password"
        placeholder="请输入密码"
        show-password
      ></el-input>
      <el-button type="primary" plain @click="register">注册</el-button>
    </div>
  </div>
</template>
<script>
import { login, register } from "api/user";
export default {
  name: "Login",
  components: {},
  data() {
    return {
      email: "",
      password: "",
      username: "",
      route: {
        path: "management",
        component: () => import("views/main/management/Management.vue")
      }
        
    };
  },
  methods: {
    async login() {
      const res = await login({ email: this.email, password: this.password });
      if (res.code == 200) {
        this.$store.commit("updateUser", res.data);
        this.$message.success("登录成功");
        if (res.data.role == 1){
            this.$router.addRoute("Main",this.route);
        }
        this.$router.push("/main/upload");
      } else this.$message.error(res.msg);
    },
    async register() {
      const res = await register({
        email: this.email,
        password: this.password,
        username: this.username,
      });
      if (res.code == 200) this.login();
      else this.$message.error(res.msg);
    },
  },
};
</script>
<style scoped>
.login {
  width: 300px;
  margin: 100px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
.register {
  width: 300px;
  margin: 200px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
</style>
