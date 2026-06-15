use std::fs;

fn main() {
    let path = "legacy/lineage_branch_jay_joy_sophia_v0_1.json";
    let expected = "4de74d74b1d7d5d493b7d915df3c06a3159ab7941d203fcdc6f0d80abeff7b16";

    let bytes = fs::read(path).expect("FAILED_TO_READ_FILE");

    let digest = sha256::digest(&bytes);

    println!("PATH={}", path);
    println!("BYTES={}", bytes.len());
    println!("SHA256_RECOMPUTED={}", digest);
    println!("SHA256_EXPECTED={}", expected);

    if digest == expected {
        println!("RUST_REPLAY_VERIFY=PASS");
        println!("IMPLEMENTATION_INDEPENDENCE=TRUE");
    } else {
        println!("RUST_REPLAY_VERIFY=FAIL");
        println!("IMPLEMENTATION_INDEPENDENCE=FALSE");
        std::process::exit(1);
    }
}
