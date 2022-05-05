<template>
  <main>
    <form @submit.prevent="register">
      <div class="mb-2">
        <label for="email" class="form-label">Email address</label>
        <input type="email" id="email" class="form-control" v-model="form.email" />
      </div>
      <div class="mb-2">
        <label for="password" class="form-label">Password</label>
        <input type="password" class="form-control" id="password" v-model="form.password" />
      </div>
      <div class="mb-2">
        <label for="token" class="form-label">token</label>
        <input type="token" class="form-control" id="token" v-model="form.token" />
      </div>

      <button type="submit" class="btn btn-primary">register</button>
    </form>
    <label v-if="isLoading">loading...</label>
    <label>{{msg}}</label>
  </main>
</template>

<script>
import { register } from "../services";
export default {
  data: () => ({
    form: {
      email: "earth@mail.com",
      password: "1234",
      token: "asfsv%SD%AID!@3b2",
    },
    msg: "",
    isLoading: false,
  }),
  methods: {
    async register() {
      try {
        this.isLoading = true;
        const resp = (await register(this.form)).data;

        this.msg = "saved";
        this.isLoading = false;
      } catch (err) {
        this.isLoading = false;
        console.error(err);
        this.msg = "error";
      }
      this.form.email = "";
      this.form.password = "";
      this.form.token = "";
    },
  },
};
</script>

<style scoped>
.img-wrapper {
  display: flex;
  justify-content: center;
  margin-bottom: 50px;
}
img {
  border-radius: 40%;
}
form {
  margin: auto;
  width: 300px;
}
</style>