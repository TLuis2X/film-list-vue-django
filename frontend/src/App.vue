<template>
  <div class="container pt-3">

    <div class="h1 text-center border rounded bg-light p-2 mb-3">
      Film List
    </div>

    <!-- <div class="mb-3"><u>Response data</u>:</div>
    <pre>{{ response_data }}</pre> -->

    <FilmList />

  </div>
</template>

<script>
import FilmList from './components/FilmList.vue';

export default {
  components: {
    FilmList,
  },
  data() {
    return {
      response_data: "",
    };
  },
  async mounted() {
    const response = await fetch("http://localhost:8000/api/film/1");
    this.response_data = await response.json();
  },
};
</script>
