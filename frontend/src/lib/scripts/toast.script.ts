import { toast } from 'svelte-sonner';

export function displayErrorToast(message: string) {
	return toast.error(message);
}

export function displaySuccessToast(message: string) {
	return toast.success(message);
}

export function displayGeneralErrorToast() {
	return toast.error('An unexpected error occurred. Please try again later.');
}

export function displayGeneralSuccessToast() {
	return toast.error('The operation was successfully completed.');
}
