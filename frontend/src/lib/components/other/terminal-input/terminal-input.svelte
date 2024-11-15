<script lang="ts">
	import { CornerDownLeft } from 'lucide-svelte';

	let { submit }: { submit: (value: string) => void } = $props();

	let textarea: HTMLTextAreaElement | null;
	let value = $state('');

	function handleKeydown(event: KeyboardEvent) {
		if (event.key === 'Enter') {
			event.preventDefault();

			if (event.shiftKey) {
				if (textarea) {
					const cursorPos = textarea.selectionStart ?? 0;

					textarea.value =
						textarea.value.substring(0, cursorPos) + '\n' + textarea.value.substring(cursorPos);
					textarea.selectionStart = cursorPos + 1;
					textarea.selectionEnd = cursorPos + 1;
					textarea.style.height = 'auto';
					textarea.style.height = `${textarea.scrollHeight}px`;
				}
			} else {
				handleSubmit(event);
			}
		}
	}

	function handleInput() {
		if (textarea) {
			textarea.style.height = 'auto';
			textarea.style.height = `${textarea.scrollHeight}px`;
		}
	}

	function handleSubmit(event: Event) {
		event.preventDefault();

		if (!value.trim()) {
			return;
		}

		submit(value);

		value = '';

		if (textarea) {
			textarea.value = '';
			textarea.style.height = 'auto';
			textarea.style.height = `${textarea.scrollHeight}px`;
		}
	}
</script>

<form class="bg-muted/75 flex gap-2 rounded-xl p-4" onsubmit={handleSubmit}>
	<span class="text-green-500">~user % </span>

	<textarea
		class="placeholder:text-muted-foreground grow resize-none border-none bg-transparent outline-none"
		rows="1"
		bind:value
		bind:this={textarea}
		onkeydown={handleKeydown}
		oninput={handleInput}
	></textarea>

	<CornerDownLeft class="text-foreground/50 mt-auto" />
</form>
