<template>
  <div id="film-frame">

    <h1>{{ film.title }}</h1>
    <h5>
      Released Date: {{ film.release_date }}, Box Office: ${{ film.box_office }}
    </h5>
    <p>{{ film.description }}</p>

    <button @click="deleteFilm(film.id)">Delete</button>

  </div>
</template>

<script>
export default {
  props: ['film', 'deleteFilm'],
  methods: {

  },
  computed: {

  }
}
</script>

<style scoped>
#film-frame {
  border: 2px solid red;
}
</style>