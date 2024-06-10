let
    pkgs = import <nixpkgs> {};
in pkgs.mkShell {
	nativeBuildInputs = with pkgs.buildPackages; [
        swiProlog
		python3
	];
    packages = [
        (pkgs.python3.withPackages (python-pkgs: [
            python-pkgs.colorama
        ]))
    ];
}