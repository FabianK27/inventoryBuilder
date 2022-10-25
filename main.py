from typing import *
import os

header = "cloudsandboxes:\n\tchildren:\n"

def read_to_dict(sb_list: str) -> Dict[str, Dict[str, str]]:
    out: Dict[str, Dict[str, str]] = {}
    with open(sb_list) as csbs:
        lines = csbs.readlines()
        for line in lines:
            name, ip = line.strip("\n").split(":")
            team = name.split("-")[0]
            if not team in out.keys():
                out[team] = {name: ip}
            else:
                out[team][name] = ip

        return out

def write_inventory(sb_dict: Dict[str, Dict[str, str]], outputfile: str, header: str) -> None:
    with open(outputfile, "w") as f:
        f.write(header)
        for team in sb_dict.keys():
            f.write("\t\t{}:\n\t\t\thosts:\n".format(team))
            for sb, ip in sb_dict[team].items():
                f.write("\t\t\t\t{}:\n\t\t\t\t\tansible_host: {}\n".format(sb, ip))


if __name__ == '__main__':
    sbdict=read_to_dict("cloudsbs.txt")
    print(sbdict)
    write_inventory(sbdict, "inventory.yaml", header)