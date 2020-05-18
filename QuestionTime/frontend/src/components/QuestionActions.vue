<template>
    <div class="question-actions mb-2">
        <router-link
                :to="{name:'question-editor', params:{slug:this.slug}}"
                class="btn btn-sm btn-outline-secondary mr-1"
        >Edit
        </router-link>
        <button
                class="btn btn-sm btn-outline-danger mr-1"
                @click="deleteQuestion"
        >Delete
        </button>
    </div>
</template>

<script>
    import {apiService} from "../common/api.service";

    export default {
        name: "QuestionActions",
        props: {
            slug: {
                type: String,
                required: true
            }
        },
        methods: {
            async deleteQuestion() {
                let endpoint = `/api/questions/${this.slug}/`;
                try {
                    await apiService(endpoint, "DELETE");
                    this.$router.push("/");
                } catch (error) {
                    console.log(error)
                }
            }
        }
    }

</script>

<style scoped>

</style>