<template>
  <div id="film-frame" class="card w-100 mb-4"> 
    <div class="card-body">
      <h1>{{ film.title }}</h1>
      <h5>
        Released Date: {{ film.release_date }}, Box Office: ${{ film.box_office }}
      </h5>
      <p>{{ film.description }}</p>

      <div class="d-grid gap-2 d-md-flex justify-content-md-end">
        <button class="btn btn-danger me-md-2" @click="deleteFilm(film.id)">Delete</button>

        <EditFilmModal :film="film" @update-film="onEditFilm" />
      </div>
    </div>
  </div>
</template>

<script>
import EditFilmModal from './EditFilmModal.vue'

export default {
  props: ['film', 'deleteFilm'],
  components: {
    EditFilmModal,
  },
  methods: {
    onEditFilm(updatedFilm) {
      this.$emit('update-film', updatedFilm);
    },
  },
  computed: {

  }
}
</script>

<style scoped>

</style>