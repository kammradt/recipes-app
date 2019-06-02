<template>
  <v-app>
    <v-toolbar dark class="primary" flat>
      <v-toolbar-title>Receitinhas top</v-toolbar-title>
      <v-spacer />
      <nuxt-link to="/recipes/add">
        <v-btn outline>Add</v-btn>
      </nuxt-link>
    </v-toolbar>
    <br />
    <v-layout align-start justify-start row wrap>
      <template v-for="recipe in recipes">
        <RecipeCard :key="recipe.id" :on-delete="deleteRecipe" :recipe="recipe">
        </RecipeCard>
      </template>
    </v-layout>
  </v-app>
</template>

<script>
import RecipeCard from '~/components/RecipeCard.vue'

export default {
  components: {
    RecipeCard
  },
  head() {
    return {
      title: 'Recipes list'
    }
  },
  data() {
    return {
      recipes: []
    }
  },
  async asyncData({ $axios, params }) {
    try {
      const recipes = await $axios.$get(`/recipes/`)
      return { recipes }
    } catch (e) {
      return { recipes: [] }
    }
  },
  methods: {
    async deleteRecipe(RecipeId) {
      try {
        await this.$axios.$delete(`/recipes/${RecipeId}/`) // delete recipe
        const newRecipes = await this.$axios.$get('/recipes/') // get new list of recipes
        this.recipes = newRecipes // update list of recipes
      } catch (e) {
        // eslint-disable-next-line no-console
        console.log(e)
      }
    }
  }
}
</script>
