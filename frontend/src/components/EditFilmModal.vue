<template>
  <div>

    <button type="button" class="btn btn-primary" data-bs-toggle="modal" :data-bs-target="'#staticBackdrop2'+film.id">
      Edit Film
    </button>

    <div class="modal fade" :id="'staticBackdrop2'+film.id" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">

          <div class="modal-header">
            <h1 class="modal-title fs-5" id="staticBackdropLabel">Edit Film Details Here</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>

          <div class="modal-body">
            <form @submit.prevent="saveChanges">
              <div class="mb-3">
                <label for="title" class="form-label">Title:</label>
                <input type="text" id="title" class="form-control" v-model="editedFilm.title" required>
              </div>

              <div class="mb-3">
                <label for="description" class="form-label">Description:</label>
                <textarea class="form-control" id="description" rows="3" v-model="editedFilm.description" required></textarea>
              </div>

              <div class="mb-3">              
                <label for="releaseDate" class="form-label">Release Date:</label>
                <input type="date" id="releaseDate" class="form-control" v-model="editedFilm.release_date" required>
              </div>

              <div class="mb-3">
                <label for="boxOffice" class="form-label">Box Office Amount:</label>
                <input type="number" id="boxOffice" class="form-control" v-model="editedFilm.box_office" required>
              </div>
              
            </form>
          </div>

          <div class="modal-footer">
            <!-- <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button> -->
            <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="saveChanges">Save Changes</button>
          </div>

        </div>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  props: ["film"],
  data() {
    return {
      editedFilm: { ...this.film }
    };
  },
  methods: {
    saveChanges() {
      this.$emit('update-film', this.editedFilm);
    },
  }
}
</script>