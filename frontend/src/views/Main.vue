<template>
  <!-- {{token}} -->
  <div class="content">
    <section>
      <label>available</label>
      <label>your pos</label>
      <div class="available section">{{!reserved?"4":"3"}}</div>
      <div class="parking section">{{!reserved?"-":"A1"}}</div>
    </section>
    <button
      class="btn btn-primary mt-4"
      @click.prevent="clickHandle"
    >{{!reserved?"reserve":"finish"}}</button>
    <div class="result">{{msg}}</div>
  </div>
</template>

<script>
import { reserve, checkout } from "../services";
export default {
  props: {
    token: String,
  },
  data() {
    return {
      reserved: false,
      msg: "",
    };
  },
  methods: {
    async clickHandle() {
      try {
        if (this.reserved) {
          const resp = (await checkout()).data;
          const diff = Date.now() - Date.parse(resp.date);
          const { min, sec } = this.toMinAndSec(diff);
          this.msg = `you've parked for ${min} min ${sec} sec`;

          console.log(resp);
          console.log(typeof resp.date);
        } else {
          console.log((await reserve(this.token)).data);
        }
      } catch (err) {
        console.log(err);
      }
      this.reserved = !this.reserved;
    },
    toMinAndSec(diff) {
      const sec = Math.round(diff / 1000) % 60;
      const min = Math.round(diff / 1000 / 60);
      return { min, sec };
    },
  },
};
</script>

<style scoped>
section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}
.content {
  margin: 0 auto;
  padding: 30px;
  width: 640px;
  background-color: white;
  border-radius: 20px;
}
.section {
  height: 200px;
  background-color: rgba(50, 151, 252, 0.3);
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 50px;
  color: white;
  font-size: 120px;
}
</style>