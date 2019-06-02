<template>
  <v-app>
    <v-flex pa-1 text-xs-center display-3 v-text="recipe.name" />
    <v-layout justify-space-around row fill-height>
      <v-flex xs12 md6 pa-1 pt-5>
        <img
          v-if="!preview"
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          :src="recipe.picture"
        />
        <img
          v-else
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          :src="preview"
        />
      </v-flex>

      <v-flex xs12 md6 pa-1 pt-5>
        <form @submit.prevent="submitRecipe">
          <label for>Recipe Name</label>
          <input v-model="recipe.name" type="text" />
          <div class="form-group">
            <label for>Ingredients</label>
            <input
              v-model="recipe.ingredients"
              type="text"
              name="Ingredients"
            />
          </div>
          <div>
            <label for>Food picture</label>
            <input type="file" @change="onFileChange" />
          </div>
          <div>
            <label for>Difficulty</label>
            <select v-model="recipe.difficulty" class="form-control">
              <option value="Easy">Easy</option>
              <option value="Medium">Medium</option>
              <option value="Hard">Hard</option>
            </select>
            <label for>
              Prep time
              <small>(minutes)</small>
            </label>
            <input
              v-model="recipe.prep_time"
              type="text"
              class="form-control"
              name="Ingredients"
            />
          </div>
          <div>
            <label for>Preparation guide</label>
            <textarea v-model="recipe.prep_guide" rows="8"></textarea>
          </div>
          <v-btn type="submit">Save</v-btn>
        </form>
      </v-flex>
    </v-layout>
  </v-app>
</template>

<script>
export default {
  head() {
    return {
      title: 'Add Recipe'
    }
  },
  data() {
    return {
      recipe: {
        name: ' ',
        picture: '',
        ingredients: '',
        difficulty: '',
        prep_time: null,
        prep_guide: ''
      },
      preview: ''
    }
  },
  methods: {
    onFileChange(e) {
      const files = e.target.files || e.dataTransfer.files
      if (!files.length) {
        return
      }
      this.recipe.picture = files[0]
      this.createImage(files[0])
    },
    createImage(file) {
      // let image = new Image();
      const reader = new FileReader()
      const vm = this
      reader.onload = e => {
        vm.preview = e.target.result
      }
      reader.readAsDataURL(file)
    },
    async submitRecipe() {
      const config = {
        headers: { 'content-type': 'multipart/form-data' }
      }
      const formData = new FormData()
      for (const data in this.recipe) {
        formData.append(data, this.recipe[data])
      }
      try {
        // eslint-disable-next-line no-unused-vars
        const response = await this.$axios.$post('/recipes/', formData, config)
        this.$router.push('/recipes/')
      } catch (e) {
        // console.log(e);
      }
    }
  }
}
</script>
