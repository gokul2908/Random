async function tryCatch(func, args = [], message = {}) {
  try {
    await func(...args);
    if (message.success) {
      console.log("success: ", func?.name);
    }
    return true;
  } catch (err) {
    console.log("failed:", func?.name, "/n error: ", err);
    if (message.error) console.log(message.error);
    return false;
  }
}

export default tryCatch;
