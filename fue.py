if (cx.data < 300)&(cy.data < 220):
            print("left up")
            pos_x += 0.01
            pos_y += 0.01
            set_pos(pos_x,pos_y,pos_z)
        elif (cx.data < 300)&(cy.data >= 220)&(cy.data <= 260):
            print("left right")
            pos_y += 0.01
            set_pos(pos_x,pos_y,pos_z)
        elif (cx.data < 300)&(cy.data > 260):
            print("left down")
            pos_x -= 0.01
            pos_y += 0.01
            set_pos(pos_x,pos_y,pos_z)
        elif (cx.data >= 300)&(cx.data <= 340)&(cy.data < 220):
            print("up doun")
            pos_x -= 0.01
            set_pos(pos_x,pos_y,pos_z)
        elif (cx.data > 340)&(cy.data < 220):
            print("right up")
            pos_x += 0.01
            pos_y -= 0.01
            set_pos(pos_x,pos_y,pos_z)
        elif (cx.data > 340)&(cy.data >= 220)&(cy.data <= 260):
            print("right left")
            pos_y -= 0.01
            set_pos(pos_x,pos_y,pos_z)
        elif (cx.data > 340)&(cy.data > 260):
            print("right down")
            pos_x -= 0.01
            pos_y -= 0.01
            set_pos(pos_x,pos_y,pos_z)
        elif (cx.data >= 300)&(cx.data <= 340)&(cy.data > 260):
            print("down up")
            pos_x += 0.01
            set_pos(pos_x,pos_y,pos_z)
        else:
            print("break")
            pos_x += 0.0445
            pos_y += 0.05
            pos_z -= 0.10
            set_pos(pos_x,pos_y,pos_z)
            break
