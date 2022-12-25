    const mainImg = document.querySelector(".main-img");
const images = document.querySelectorAll(".gallery-wrapper img");
const closeBtn = document.querySelector(".close");
const nextBtn = document.querySelector(".next");
const prevBtn = document.querySelector(".prev");

nextBtn.addEventListener("click", nextImg);
prevBtn.addEventListener("click", prevImg);

closeBtn.addEventListener("click", (e) => {
	mainImg.style.display = "none";
	mainImg.classList.remove("active");
});

// Creating Animation For Image Transition

const imgStyles = `animation: imgTransition 0.450s  ease-in-out`;

let showImg = document.querySelector(".main-img img");

let imagesArray = [];

let selectedImg;

// Click Next Button Function

function nextImg() {
	if (selectedImg < 0) return;
	let number = Number(selectedImg);
	let higestCount = Number(imagesArray.length - 1);
	if (number === higestCount) {
		number = 0;
	} else {
		number++;
	}
	selectedImg = number;
	showImg.src = imagesArray[selectedImg];
	addRemoveAnimation();
}

// Click Prev Button Function

function prevImg() {
	if (selectedImg < 0) return;
	let number = Number(selectedImg);
	let lowestCount = 0;
	let higestCount = Number(imagesArray.length - 1);
	if (number <= lowestCount) {
		number = higestCount;
	} else {
		number--;
	}
	selectedImg = number;
	showImg.src = imagesArray[selectedImg];
	addRemoveAnimation();
}

// Initial Click Handler

for (let image of images) {
	imagesArray.push(image.src);
	image.addEventListener("click", (e) => {
		let img = e.target;
		currentSelectedImg = imagesArray.indexOf(img.src);
		mainImg.style.display = "block";
		mainImg.classList.add("active");
		showImg.src =
			imagesArray[selectedImg !== undefined ? selectedImg : currentSelectedImg];
		selectedImg = currentSelectedImg;
	});
}

// Function for add and Remove Style Attribute

function addRemoveAnimation() {
	showImg.setAttribute("style", imgStyles);
	setTimeout(() => {
		showImg.setAttribute("style", "");
	}, 500);
}