const modules = import.meta.glob("../assets/players/*.{png,jpg,jpeg,webp,avif}", {
    eager:true, 
    query: "?url",
    import: "default"
});

const playerPictures = {};

for (const path in modules) {
    const url = modules[path];
    const file = path.split("/").pop();
    const name = file.replace(/\.(png|jpe?g|webp|avif)$/i, "");
    playerPictures[name] = url;
}

export default playerPictures;
