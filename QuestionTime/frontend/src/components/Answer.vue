<template>
    <div class="single-answer">
        <p class="text-muted">
            <strong>{{answer.author}}</strong> &#8901; {{answer.created_at}}
        </p>
        <p> {{answer.body}} </p>
        <div v-if="isAnswerAuthor">
            <router-link
                    :to="{name:'answer-editor', params:{id:answer.id}}"
                    class="btn btn-sm btn-outline-secondary mr-1"
            >Edit
            </router-link>
            <button
                    class="btn btn-sm btn-outline-danger"
                    @click="triggerAnswerDelete"
            >Delete
            </button>
        </div>
        <hr>
    </div>
</template>

<script>
    export default {
        name: "AnswerComponent",
        props: {
            answer: {
                type: Object,
                required: true
            },
            requestUser: {
                type: String,
                required: true
            }
        },
        computed: {
            isAnswerAuthor() {
                return this.answer.author === this.requestUser
            }
        },
        methods: {
            triggerAnswerDelete() {
                this.$emit("delete-answer", this.answer)
            }
        }
    }
</script>

<style scoped>
    .single-answer {

    }
</style>