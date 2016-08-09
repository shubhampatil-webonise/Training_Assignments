
//Single responsibility Class (S-SOLID) : maintains state of the current tv (vendor specific implementation)

public class TVState extends StateHandler {

    TVState(){
        this.volume = 0;
        this.channel = 0;
        this.isSwitchedOn = false;
        this.maxVolumeLimit = 100;
        this.maxChannelLimit = 60;
    }
}
